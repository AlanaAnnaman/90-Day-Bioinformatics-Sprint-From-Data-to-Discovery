# ============================================================
# ML WORKFLOW OVERVIEW - Antimicrobial Resistance (AMR) Prediction Project
# ============================================================
# 1. Define the problem: predict Resistant vs. Susceptible to ciprofloxacin,       [DONE]
#    from genomic data (E. coli)
# 2. Collect data: downloaded 15,827 E. coli genomes with lab-tested resistance    [DONE]
#    results from BV-BRC (this file handles this step)
# 3. Clean and prepare the data: removed rows with missing/unusable labels and     [DONE]
#    the "Intermediate" category; left with 8,631 genomes clearly labeled
#    Resistant or Susceptible (this file handles this step)
# 4. Feature engineering: attach real genomic information to each genome, since    [DONE]
#    the model needs clues to learn from, not just the answer - pulling
#    presence/absence of known antibiotic resistance genes per genome from
#    BV-BRC's specialty gene data (this file collects the raw data;
#    build_features.py turns it into a model-ready feature table)
# 5. Split the data into training and test sets                                   [DONE - see build_features.py]
# 6. Choose a model: compared Logistic Regression, Random Forest, XGBoost         [DONE - see build_features.py]
# 7. Train the model                                                             [DONE - see build_features.py]
# 8. Evaluate the model: accuracy 90%, 5-fold cross-validation average 90.7%      [DONE - see build_features.py]
#    (+/- 2.4%), ROC-AUC 0.92
# 9. Interpret the results: top predictive genes (CTX-M family, mphA, sul1,       [DONE - see build_features.py]
#    QacE, etc.) matched an independent statistical comparison of gene
#    prevalence between Resistant and Susceptible genomes - the model learned
#    real, biologically explainable signal, not noise
# 10. Iterate/improve: compared 3 models (similar performance, suggesting the     [DONE - see build_features.py]
#     feature set, not the algorithm, is the current ceiling); caught and fixed
#     a class-order bug in the ROC-AUC calculation
#     NEXT STEP (future work): investigate direct detection of gyrA/parC point
#     mutations at the sequence level, since this dataset's resistance appears
#     to be driven more by point mutations than acquired qnr genes (see
#     Feature Engineering notes below), which may improve recall on the
#     Resistant class (currently 72%)
#
# NOTE: this file (collect_data.py) handles Steps 2-4 part 1 - collecting the
# raw data. Feature building, modeling, and evaluation (Steps 4 part 2 - 10)
# live in build_features.py
# ============================================================


## Goal: build a model that can predict Resistant vs. Susceptible just from the bacteria's genetic information.
# Susceptible = the antibiotic worked; the bacteria were killed/stopped at a normal drug concentration
# Resistant = the antibiotic did NOT work; the bacteria survived and kept growing
# Intermediate = a middle category where the drug partially works, often only at higher doses
#   (excluded from this first model since it's a small, ambiguous category)


# ============================================================
# STEP 2: Collect data - load the raw AMR dataset downloaded from BV-BRC
# (Source: BV-BRC website, AMR Phenotypes tab, filtered to E. coli + ciprofloxacin +
#  Evidence = "Laboratory Method" only, to exclude BV-BRC's own computational predictions)
# ============================================================
import pandas as pd
import requests
import time

df = pd.read_csv("BVBRC_genome_amr.csv")

# STEP 3: Clean - keep only genomes with a clear Resistant or Susceptible label
# (drops rows with no interpreted phenotype - only a raw MIC value - and the
# ambiguous "Intermediate" category). This takes 15,827 rows down to 8,631.
df_clean = df[df["Resistant Phenotype"].isin(["Resistant", "Susceptible"])].copy()

# Take a random sample of 2,000 genomes (shuffled, not just the first N in file order,
# so we get a representative mix of Resistant/Susceptible). Chosen as a practical
# middle ground between speed and dataset size - the full 8,631 was judged not
# strictly necessary for a first working model.
df_sample = df_clean.sample(n=2000, random_state=42).reset_index(drop=True)

print("Sample breakdown:")
print(df_sample["Resistant Phenotype"].value_counts())


# ============================================================
# STEP 4 (part 1): Feature engineering - collect genomic data for each genome
#
# Background on what was tried first and why it changed:
# - Initially checked for gyrA/gyrB/parC/parE (ciprofloxacin's direct molecular
#   targets) - these are essential genes present in virtually every E. coli
#   genome regardless of resistance status, so they carry no useful signal.
# - Searched a known-Resistant genome for acquired qnr genes (plasmid-mediated
#   quinolone resistance) across all 3,433 of its annotated genes - none found,
#   suggesting this dataset's resistance is more likely driven by point
#   mutations (not detectable via simple gene presence/absence) than acquired
#   qnr genes.
# - Pivoted to pulling ALL "Antibiotic Resistance" category genes per genome
#   (BV-BRC's sp_gene endpoint) as a broader, pragmatic feature set. Genes
#   found to matter most turned out to be markers of OTHER antibiotic classes
#   (e.g. mphA/macrolides, CTX-M/beta-lactams, sul1/sulfonamides) - a real
#   phenomenon called co-selection, where bacteria carrying one
#   multidrug-resistance plasmid often carry ciprofloxacin resistance as part
#   of the same genetic package, even though none of these genes directly
#   disable ciprofloxacin itself.
#
# For each of the 2,000 sampled genomes, this asks BV-BRC's API which
# "Antibiotic Resistance" category genes it has, and saves that list.
# ============================================================
genome_gene_data = []

for i, row in df_sample.iterrows():
    genome_id = row["Genome ID"]
    url = f"https://www.bv-brc.org/api/sp_gene/?eq(genome_id,{genome_id})&limit(4000)"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            results = response.json()
            # Keep only genes tagged "Antibiotic Resistance" - filtering client-side here,
            # since the API's own property filter syntax (eq(property, Antibiotic Resistance))
            # did not match reliably, likely due to the space in the value
            genes_found = [r.get("gene") for r in results if r.get("property") == "Antibiotic Resistance" and r.get("gene")]
            genome_gene_data.append({
                "Genome ID": genome_id,
                "Resistant Phenotype": row["Resistant Phenotype"],
                "resistance_genes": ";".join(genes_found) if genes_found else ""
            })
        else:
            # Request failed (bad status code) - still record the genome with an empty
            # gene list rather than losing it entirely
            genome_gene_data.append({"Genome ID": genome_id, "Resistant Phenotype": row["Resistant Phenotype"], "resistance_genes": ""})
    except Exception:
        # Catches network errors/timeouts so one bad request doesn't crash the whole run
        genome_gene_data.append({"Genome ID": genome_id, "Resistant Phenotype": row["Resistant Phenotype"], "resistance_genes": ""})

    if (i + 1) % 100 == 0:
        print(f"Processed {i + 1} of {len(df_sample)} genomes...")
        # Save progress every 100 genomes, so nothing is lost if this run stops early
        pd.DataFrame(genome_gene_data).to_csv("genome_resistance_genes_partial.csv", index=False)

    time.sleep(0.3)  # small pause between requests, polite to the API server

# Final save - the raw collected data: one row per genome, with its gene list as a
# semicolon-separated string. This file feeds directly into build_features.py.
# Note: only 1,263 of these 2,000 genomes turned out to have any resistance-gene
# annotation at all in BV-BRC; the rest are recorded with an empty gene list and
# are excluded from modeling in build_features.py.
final_df = pd.DataFrame(genome_gene_data)
final_df.to_csv("genome_resistance_genes_2000.csv", index=False)
print("\nDone! Saved to genome_resistance_genes_2000.csv")
print(final_df.head(10))
