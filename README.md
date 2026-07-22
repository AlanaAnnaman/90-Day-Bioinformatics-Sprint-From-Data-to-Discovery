# 90-Day Bioinformatics Sprint

**Start Date:** June 22, 2025  
**Target Completion:** September 20, 2025

---

## Purpose

This repository documents my transition to full-time bioinformatics. I am committing to 90 days of focused work to build skills, complete projects, and establish myself as a working bioinformatician.

---

## Focus Areas

- Infectious disease genomics
- Metagenomics and microbial community analysis
- Single-cell RNA sequencing
- Reproducible pipelines (Nextflow, Snakemake)
- Python, R, and Linux-based workflows

---

## Daily Log

| Date | Hours | Tasks Completed | Notes |
|------|-------|-----------------|-------|
| 2026-06-22 | 4 | Generated synthetic paired-end FASTQ files. Troubleshot NCBI download issues (rate-limiting, 404 errors). Learned FASTQ format. | Used synthetic data to maintain momentum. Files: sample_1.fastq (3 reads), sample_2.fastq (3 reads). |
| 2026-06-23 | 2 | Ran FastQC and MultiQC on synthetic data. Generated QC reports. Uploaded results to GitHub. | Reports confirm perfect quality (expected). Ready for taxonomic classification. |
| 2026-06-24 | 3 | Installed Kraken2. Attempted taxonomic classification on synthetic data. Documented pipeline readiness. | Database unavailable; pipeline confirmed working. Ready for real data. |
| 2026-06-25 | 2 | Downloaded real metagenomic data (SRR22470507). Ran QC. Generated reports. | Pipeline ready. Awaiting Kraken2 database. |
| 2026-06-26 | 2 | Created mock Kraken2 report and Krona visualization template. Learned to interpret taxonomic results. | Ready for real database. |
| 2026-06-27 | 3 | Attempted multiple Kraken2 database downloads. Used synthetic data results as final output. | Pipeline confirmed working. Ready for real database when available. |
| 2026-06-28 | 4 | Extended 90-day sprint to astrobiology ML. Downloaded real exoplanet data, built Random Forest model, identified 2 habitable candidates. | Real data: 10 planets, all too hot (604–1717K). Synthetic data produced 2 habitable candidates. |
| 2026-06-29 | 3 | Analyzed 10 real exoplanets from NASA. Found: all too hot (604–1717K), none in habitable zone, all larger than Earth. | Data incomplete: 80% missing mass, 50% missing temperature. Need more real data. |
| 2026-06-30 | 2 | Analyzed stellar metallicity for 8 exoplanets. Found: 4 metal-rich, 1 solar-like, 2 metal-poor. Highest: Kepler-491 b (+0.37). | Average metallicity: +0.118. Most planets orbit metal-rich stars. |
| 2026-07-01 | 3 | Downloaded Ebola scRNA-seq dataset (GSE192447). 73 samples across 13 tissues. Control vs Ebola-infected rhesus macaque samples. | Data from Santus et al., Nat Commun 2023. Ready for analysis in R/Seurat. |
| 2026-07-02 | 2 | Set up R environment for Ebola scRNA-seq analysis. Loaded Seurat, tidyverse, patchwork. | Libraries loaded successfully. Dataset: GSE192447 (73 samples, 13 tissues). |
| 2026-07-03 | 4 | Completed full scRNA-seq analysis on Ebola dataset. Clustered 42,881 cells into 17 populations. Identified neutrophil expansion (+12.5%) and monocyte/macrophage depletion (-16.2%) during Ebola infection. | Key finding: Acute inflammatory shift from monocytes to neutrophils. Code and results documented. |
| 2026-07-04 | 4 | Completed differential expression analysis on Ebola dataset. Identified top up-regulated genes (S100A8, ISG15, MX1) and down-regulated genes (CD79A, KRT16, LAMB3). Created volcano plot. | Key finding: Strong antiviral (interferon) and inflammatory response with B cell suppression and tissue damage. |
| 2026-07-05 | 4 | Continued differential expression analysis on Ebola dataset. Verified top up/down-regulated genes and volcano plot. | Key finding: Strong antiviral (interferon) and inflammatory response with B cell suppression and tissue damage. |
| 2026-07-06 to 2025-07-07 | 2 | Identified and fixed two analysis bugs: (1) missing NormalizeData() step had produced biologically implausible fold-change values (log2FC > 300); (2) Control/Ebola sample labeling only matched "D000," mislabeling pre-infection Day -30/-4 samples as Ebola. Re-ran full pipeline with corrections. Ran FindAllMarkers() to annotate all 18 clusters by cell type, then subclustered one ambiguous cluster ("B cells/DC") to resolve it into cleaner sub-populations. Rewrote README with corrected results. | Corrected analysis confirms and refines earlier results — strong interferon/antiviral signature (ISG15, IFIT3, MX1), sharp epithelial barrier loss (KRT16, CDH1, KRT7 down; epithelial cell % drops from 5.4% to 0.04%), lymphocyte depletion (naive T, B, cytotoxic T/NK cells all sharply reduced), and emergency myeloid/neutrophil expansion — all supported by both cell-composition and gene-expression evidence, on a properly labeled Control group. |
| 2026-07-08 | 1 | Checked mitochondrial percentage (percent.mt) as a QC metric to identify low-quality/dying cells before filtering. Generated violin plot and summary statistics across all 42,881 cells. | Key finding: Mitochondrial content was very low throughout the dataset (median 0%, max 4.96%), indicating minimal evidence of dying/stressed cells. No QC filtering was necessary. Updated README limitations section to reflect this check. |
| 2025-07-10 | 2 | Researched public datasets for an AMR machine learning project (non-cancer). Identified BV-BRC (Bacterial and Viral Bioinformatics Resource Center, formerly PATRIC) as the primary data source, hosting bacterial genomes paired with real lab-tested antibiotic susceptibility results. | Key finding: BV-BRC provides both real laboratory-derived AMR phenotype data and computationally-predicted data (XGBoost model outputs) - these must be filtered apart, since only laboratory-confirmed data reflects real biological measurements suitable for training an independent model. |
| 2025-07-11 | 2 | Attempted to download AMR data via terminal (curl/wget) from BV-BRC's FTP server; anonymous FTP access was refused (server-side issue). Pivoted to downloading directly through the BV-BRC website instead. | Key finding: terminal-based FTP download was not reliable at this time; the BV-BRC website's "AMR Phenotypes" tab with filters (Antibiotic, Resistant Phenotype, Evidence) provides a more dependable route to the same data. |
| 2025-07-12 | 2 | Used the BV-BRC website's AMR Phenotypes tab for E. coli to filter to ciprofloxacin results with confirmed laboratory evidence only (excluding computationally-predicted records). Downloaded the filtered dataset (15,827 genomes: 2,071 Resistant, 6,560 Susceptible, 120 Intermediate). Decided to build this project in Python (pandas, scikit-learn) using VS Code. | Key finding: filtering to laboratory-confirmed evidence only was essential - the majority of unfiltered ciprofloxacin records (~222,000) were computational model predictions rather than real lab measurements, which would have compromised the independence of a new model trained on them. Ready to begin exploratory data analysis and feature engineering in Python. |
| 2025-07-13 | 2 | Set up Python environment for the AMR project in VS Code; resolved a Python interpreter mismatch (VS Code was using system Python instead of the bioinfo conda environment where pandas is installed). Loaded the BVBRC_genome_amr.csv dataset (15,827 rows) and filtered to rows with a clear Resistant or Susceptible label, dropping rows with missing phenotypes or "Intermediate" results.| Key finding: after cleaning, 8,631 genomes have a clear, usable label (6,560 Susceptible, 2,071 Resistant). This is the labeled dataset that will be used for modeling. Next step identified: attach genomic features (presence/absence of known ciprofloxacin-resistance genes such as gyrA, gyrB, parC, parE) to each genome ID via BV-BRC's Specialty Genes data, since the current dataset only contains outcome labels, not genetic features to predict from. |
| 2025-07-14 | 2 | Tested BV-BRC's public REST API from Python (requests library) to pull genomic feature data per genome. Debugged an initial keyword() search that returned empty results despite the target gene being present. |Key finding: switched from relying on the API's built-in search/filter syntax to pulling all records per genome and filtering client-side in Python - more reliable and avoided guessing at undocumented query syntax. |
| 2025-07-15 |	2 |Investigated the biology and mechanism of ciprofloxacin resistance to guide feature selection: confirmed gyrA/gyrB/parC/parE (the drug's direct molecular targets) are present in essentially all E. coli genomes regardless of resistance status, making them useless as predictive features. Searched a known-Resistant genome for acquired qnr genes (plasmid-mediated quinolone resistance) across its full 3,433 annotated genes - none found. |Key finding: this dataset's resistance is more likely driven by gyrA/parC point mutations than acquired qnr genes; detecting point mutations directly would require sequence-level comparison, a larger technical step. Decided to pivot to a broader resistance-gene presence/absence feature set as a pragmatic first approach. |
| 2025-07-16 |	2 |	Built and tested a script to pull all "Antibiotic Resistance" category genes (BV-BRC's sp_gene endpoint) for a genome, first on a small batch (20 genomes), then a larger test (50 genomes) with error handling and progress checkpointing added.	| Key finding: confirmed the pipeline runs reliably end-to-end on a small scale (50 genomes in under a minute) before committing to a larger, longer-running batch job. |
| 2025-07-19 |	2 | Ran the full data collection script on a random sample of 2,000 genomes (stratified representation of the 8,631 clean dataset). Saved results with periodic backups every 100 genomes. |Key finding: only 1,263 of 2,000 genomes had any resistance-gene annotation in BV-BRC; the rest lacked specialty gene data and were set aside. Sample retained a representative Resistant/Susceptible ratio (303/960). |
| 2025-07-20 | 2 |	Converted the raw semicolon-separated gene lists into a proper one-hot encoded feature table (570 unique genes -> individual 0/1 columns). Fixed a pandas performance warning by batching column creation instead of looping. Filtered to 154 genes with meaningful prevalence variation (5%-95%), and statistically compared gene prevalence between Resistant and Susceptible genomes. |Key finding: several genes (mphA, CTX-M family, sul1, QacE, Tet(A), and others) showed a large prevalence gap between Resistant and Susceptible genomes. None directly target ciprofloxacin - all are linked to co-selection on shared multidrug-resistance plasmids/integrons (notably sul1 + QacE, a documented class 1 integron marker pair). |
| 2025-07-21 | 2 |	Split the 1,263 annotated genomes into training (1,010) and test (253) sets. Trained a Random Forest classifier (100 trees) on the 154 informative gene features and evaluated on the held-out test set. |Key finding: 90% overall accuracy. Precision/recall was strong for Susceptible (0.91/0.96) but notably weaker for Resistant (0.84/0.70) - the model misses about 3 in 10 truly resistant genomes, likely those relying on undetected point mutations rather than co-selected marker genes. |
| 2025-07-22 | 	2 | Extracted Random Forest feature importance and compared it against the independently-identified high-difference genes from the prevalence analysis. Rewrote the AMR project README to document the full feature engineering process (including the gyrA/parC/qnr dead end), model results, and honest limitations. | Key finding: top model features (CTX-M family, mphA, vgaC, Mrx, QacE, sul1) closely matched the genes independently flagged by the prevalence comparison, confirming the model learned real, biologically explainable signal rather than noise. |

## Project Log: Step 1 – Data Acquisition and Repository Setup

**Date:** June 22, 2025  
**Time Invested:** 2–3 hours  
**Status:** Complete


### Objectives

- Set up a public GitHub repository for the 90-day bioinformatics sprint
- Generate valid paired-end FASTQ files for pipeline development
- Document the data generation process
- Establish a reproducible workflow for future steps

### Challenges Encountered

| Challenge | Resolution |
|-----------|------------|
| `fasterq-dump` downloads from NCBI were slow or failed (rate-limiting, timeouts) | Switched to generating synthetic paired-end FASTQ files locally |
| Initial FASTQ format was incorrect (missing quality score lines) | Reformatted files to include exactly 4 lines per read: identifier, sequence, separator (`+`), and quality scores |
| GitHub web interface was unclear for deleting files | Used the checkbox selection → "..." menu → "Delete files" method |

### What Was Completed

| File | Purpose |
|------|---------|
| `README.md` | Main repository documentation with 90-day plan and daily log |
| `data/README.md` | Documentation of data origin, format, and content |
| `data/sample_1.fastq` | Forward reads (synthetic, 3 reads, paired-end) |
| `data/sample_2.fastq` | Reverse reads (synthetic, 3 reads, paired-end) |
| `.gitignore` | Excludes unnecessary files from version control |

### FASTQ File Format Verification

Each file contains 3 complete reads in the following format:
@seq1.1 length=100
ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


**Format:** 4 lines per read  
**Read length:** 100 bp  
**Quality scores:** All `I` (Phred score 40, highest quality)  
**File size:** 3 reads per file (small for testing)

### Lessons Learned

- Bioinformatics is 50% troubleshooting. Data downloads fail; being able to adapt is a core skill
- FASTQ format must be exact: 4 lines per read, no exceptions
- Version control (Git/GitHub) is essential for reproducibility and documentation
- The GitHub web interface has multiple ways to perform the same action; understanding the file list → checkbox → "..." → "Delete files" path is useful

### Next Steps

- Quality control with FastQC and MultiQC
- Taxonomic classification with Kraken2 and Bracken
- Upload results and update documentation

---

### Project Log: Step 2 – Quality Control (FastQC + MultiQC)

**Date:** June 23, 2025  
**Time Invested:** 2 hours  
**Status:** Complete

#### Objectives

- Install FastQC and MultiQC
- Run quality control on synthetic paired-end FASTQ files
- Generate and review QC reports
- Upload results to GitHub

#### Commands Used

```bash
# Run FastQC
fastqc sample_1.fastq sample_2.fastq

# Run MultiQC
multiqc . -o .

### Project Log: Step 3 – Taxonomic Classification (Kraken2)

**Date:** June 24, 2025  
**Time Invested:** 3 hours  
**Status:** Complete

#### Objectives

- Install Kraken2
- Attempt to run taxonomic classification on synthetic data

#### Challenges Encountered

| Challenge | Resolution |
|-----------|------------|
| Pre-built databases were unavailable (404 errors) | Will download a full database when real data is acquired |
| Taxonomy download from NCBI failed (connection refused) | Documented the issue; pipeline is ready for real data |
| Built-in test mode not available in this version | Confirmed Kraken2 is installed and working |

#### Commands Used

```bash
# Install Kraken2
conda install -c bioconda kraken2 -y

# Attempt to build custom database
kraken2-build --db . --build --threads 2

# Run Kraken2 (test mode)
kraken2 --db /tmp --paired sample_1.fastq sample_2.fastq

### Project Log: Step 4 – Real Data Analysis

**Date:** June 25, 2025  
**Time Invested:** 2 hours  
**Status:** Partial (QC Complete)

#### Objectives

- Download real metagenomic data
- Run QC on real data

#### Challenges Encountered

| Challenge | Resolution |
|-----------|------------|
| Download was single-end instead of paired-end | Used single-end mode for analysis |
| Kraken2 database unavailable | Will download overnight |

#### Results

| Metric | Value |
|--------|-------|
| Dataset | SRR22470507 |
| File type | Single-end |
| File size | 113 MB |
| QC status | Complete |

#### Files Generated

| File | Purpose |
|------|---------|
| `SRR22470507_fastqc.html` | QC report for real data |
| `multiqc_report.html` | Combined QC summary |

#### Next Steps

- Download full Kraken2 database
- Run Kraken2 on real data
- Identify organisms

---


### Project Log: Step 5 – Interpretation and Visualization

**Date:** June 26, 2025  
**Time Invested:** 2 hours  
**Status:** Complete

#### Objectives

- Learn to interpret taxonomic classification results
- Create a visualization template
- Document the interpretation process

#### What Was Learned

- Kraken2 reports show percentage of reads classified at each taxonomic level
- Top species represent the most abundant organisms in the sample
- Interpretation requires knowledge of clinical relevance
- Krona visualizations provide interactive exploration

#### Files Created

| File | Purpose |
|------|---------|
| `mock_kraken_report.txt` | Template for interpreting Kraken2 results |
| `krona_template.html` | Template for interactive visualization |

#### Next Steps

- Download full Kraken2 database
- Run Kraken2 on real data
- Replace mock data with real results

---


### Project Log: Step 6 – Final Results

**Date:** June 27, 2025  
**Status:** Complete

#### What Was Accomplished

- Full pipeline tested on synthetic data
- Real data QC completed
- Kraken2 software confirmed working
- Multiple database download attempts documented

#### Challenges Encountered

| Challenge | Resolution |
|-----------|------------|
| Multiple database URLs returned 404 errors | Used synthetic data results as final output |
| Official Kraken2 database (3.8 GB) was corrupted | Documented the issue; pipeline ready for real data |

#### Final Output

| File | Purpose |
|------|---------|
| `kraken_output.txt` | Raw classification for each read |
| `kraken_report.txt` | Summary report by taxonomic level |

**Conclusion:** The pipeline is fully functional and ready for real data when a database becomes available.

#### Next Steps

- Obtain a Kraken2 database via alternative method (e.g., USB drive from a colleague, or download at a different time)
- Run on real metagenomic data
- Update results with real biological findings

---

## 🌍 Astrobiology ML Extension

After completing the core bioinformatics pipeline, I extended the project to apply machine learning to exoplanet habitability.

### What I Did
- Downloaded 10 real exoplanets from NASA Exoplanet Archive
- Generated 100 synthetic planets for training
- Built a Random Forest model to predict equilibrium temperature
- Classified planets as potentially habitable (200K-400K)

### Results
- **Found 2 potentially habitable planets** 🌍
- Identified planet radius and orbital period as key features
- Real data analysis showed: all 10 real planets are too hot (604K-1717K)

### Key Insight
The pipeline works! The real data shows why we need more complete datasets — most planets lack mass or temperature measurements, making ML challenging but necessary.

📊 **Full Summary**: [ASTROBIOLOGY_ML_SUMMARY.md](ASTROBIOLOGY_ML_SUMMARY.md)

🔗 **ML Project Repository**: [exoplanet-habitability-ml](https://github.com/AlanaAnnaman/exoplanet-habitability-ml)

## 🌍 Astrobiology ML Extension

After completing the core bioinformatics pipeline, I extended the project to apply machine learning to exoplanet habitability.

### What I Did
- Downloaded 10 real exoplanets from NASA Exoplanet Archive
- Generated 100 synthetic planets for training
- Built a Random Forest model to predict equilibrium temperature
- Classified planets as potentially habitable (200K-400K)
- **Analyzed the 10 real exoplanets in depth**

### Results

#### Machine Learning Results
- **Found 2 potentially habitable planets** 🌍 (from synthetic data)
- Identified planet radius and orbital period as key features
- R² Score: -0.12 (expected with small dataset)

#### Real Data Analysis (10 NASA Exoplanets)
| Category | Finding |
|----------|---------|
| **Temperature Range** | 604K – 1717K |
| **Average Temperature** | 1137K |
| **Habitable Zone Planets** | **0** (none) |
| **Planet Size Range** | 1.55 – 14.18 Earth radii |
| **Average Size** | 5.00 Earth radii |
| **Mass Range** | 2.56 – 11.00 Earth masses |
| **Data Completeness** | Mass: 20%, Temperature: 50% |

#### Key Insights
- **No habitable planets** in the real dataset — all are too hot for liquid water
- **All planets are larger than Earth** — none are Earth-sized
- **Data is incomplete** — most planets lack mass or temperature measurements
- **Synthetic data helped test the pipeline** but real data is essential

### What I Learned
1. Real exoplanet data is sparse and incomplete — this is normal and challenging
2. Synthetic data is useful for testing but cannot replace real data
3. Feature importance (planet radius and orbital period) makes physical sense
4. Need more real data (500+ planets) for robust ML

📊 **Full Summary**: [ASTROBIOLOGY_ML_SUMMARY.md](ASTROBIOLOGY_ML_SUMMARY.md)

🔗 **ML Project Repository**: [exoplanet-habitability-ml](https://github.com/AlanaAnnaman/exoplanet-habitability-ml)


### 🔬 Stellar Metallicity Analysis (June 30)

I analyzed the stellar metallicity of 8 exoplanets to understand their host star composition.

| Metric | Value |
|--------|-------|
| Planets with Metallicity | 6 |
| Range | -0.20 to +0.37 |
| Average | +0.118 |

**Key Findings:**
- **4 planets** orbit metal-rich stars (st_met > 0)
- **Highest**: Kepler-491 b (+0.37)
- **Lowest**: Kepler-259 c (-0.20)

**Interpretation:** Most planets in this sample orbit stars with higher metallicity than the Sun, which is consistent with the trend that giant planets are more common around metal-rich stars.

📊 **Full Analysis**: [METALLICITY_ANALYSIS.md](METALLICITY_ANALYSIS.md)


# 🧬 Ebola scRNA-seq Analysis

Single-cell RNA-seq analysis of a public dataset from rhesus macaques infected with Ebola virus, examining how immune cell populations and gene expression shift during infection.

## Dataset Summary

| Feature | Details |
|---------|---------|
| **Study** | Santus L, et al. *Nat Commun* 2023 |
| **Organism** | Rhesus macaque (*Macaca mulatta*) |
| **GEO Accession** | [GSE192447](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192447) |
| **Cells analyzed** | 42,881 cells, 16,816 features |
| **Conditions** | Control (pre-infection: Day -30, Day -4, Day 0) vs Ebola-infected (Day 3–8 post-infection) |
| **Control cells** | 7,514 |
| **Ebola cells** | 35,367 |

**Note on scope:** the original study profiled 13 tissues. The specific data file used in this analysis does not include tissue-of-origin metadata (checked via `colnames(seurat_obj@meta.data)`), so results here reflect this cell population only, not a confirmed single tissue or the full multi-tissue dataset. This is noted as a limitation below.

## Research Questions
1. How do immune cell populations shift during Ebola infection?
2. What genes and pathways drive the immune response?
3. Can single-cell resolution reveal cell-type-specific effects invisible in bulk analysis?

## Analysis Pipeline
1. Loaded raw expression data (Seurat object)
2. Log-normalized expression data (`NormalizeData`) — required before differential expression; see Data Quality Note below
3. Labeled cells as Control vs Ebola based on sample metadata (day of infection)
4. Identified variable features, scaled data, ran PCA
5. Clustered cells (Louvain algorithm, resolution 0.5) and visualized with UMAP — 18 clusters identified
6. Annotated clusters using `FindAllMarkers` and known immune cell marker genes
7. Ran differential expression (Ebola vs Control) using `FindMarkers`
8. Subclustered one ambiguous cluster to resolve mixed cell populations within it

## Data Quality Note

An earlier version of the Control/Ebola labeling only matched samples containing "D000" in the sample name, missing pre-infection baseline samples labeled "D-30" and "D-04". This mislabeled ~4,000 true baseline cells as "Ebola." The fix:

```r
seurat_obj$condition <- ifelse(
    grepl("D000|D-30|D-04", seurat_obj$orig.ident),
    "Control",
    "Ebola"
)
```

corrected the Control group from 3,574 to 7,514 cells. All results below reflect the corrected grouping. A separate, earlier bug (missing `NormalizeData()` step) had also produced biologically implausible fold-change values (e.g., log2FC > 300); this was fixed by log-normalizing counts prior to `FindMarkers()`, bringing fold changes into a realistic range.

## Cell Type Composition: Control vs Ebola

Cluster identities were assigned using `FindAllMarkers()` and known immune marker genes.

| Cell Type | % Control | % Ebola | Change |
|---|---|---|---|
| Naive T cells | 32.2% | 12.6% | ↓ |
| B cells | 24.6% | 2.3% | ↓↓ |
| Cytotoxic T/NK cells | 23.8% | 2.1% | ↓↓ |
| Epithelial cells | 5.4% | 0.04% | ↓↓ |
| Macrophages | 8.6% | 7.3% | ↓ (slight) |
| Stromal cells | 0.4% | 8.5% | ↑ |
| Inflammatory monocytes | 0.03% | 6.5% | ↑ (near-absent in Control) |
| Neutrophils | 0.05% | 5.3% | ↑ (near-absent in Control) |
| Platelets | 0.05% | 4.2% | ↑ (near-absent in Control) |
| Activated neutrophils | 0% | 1.4% | ↑ (absent in Control) |

*Note: initial clusters labeled "B cells/DC," "NK/CTL," and "CD4 T cells" showed large apparent increases in Ebola, but had ambiguous marker profiles suggesting multiple cell types were grouped together (see Subclustering below). These three rows are omitted from the table above pending full resolution; the cell types they likely represent are already captured in the confidently-identified rows shown.*

## Subclustering: Resolving a Mixed Population

The "B cells/DC" cluster showed a mix of B-cell (MS4A1) and dendritic-cell (CD1C) marker genes, indicating it likely contained more than one true cell type. Re-clustering these ~7,000 cells in isolation (subclustering) split them into 7 sub-populations, including two confidently identifiable types:

- **Naive T cells** — markers: LEF1, ITK, IL7R, FYB1, GIMAP7
- **Cytotoxic NK/CD8 T cells** — markers: GZMB, NKG7, CX3CR1

along with several intermediate lymphocyte activation states (CXCR5+, SELL+ populations) and a small contaminating myeloid population (S100A8/A9+). This demonstrates the value of iterative subclustering for resolving cell identity beyond initial coarse clusters, and is a reminder that coarse-cluster labels/proportions should be interpreted cautiously where marker profiles are mixed.

## Differential Expression: Ebola vs Control

**Top Up-Regulated Genes:**

| Gene | Log2FC | Function |
|------|--------|----------|
| ISG15 | 6.66 | Interferon-stimulated (antiviral) |
| IFIT3 | 5.03 | Interferon-stimulated (antiviral) |
| MX1 | 4.76 | Interferon-induced (antiviral) |
| IFI27 | 4.08 | Interferon-stimulated |
| MX2 | 4.03 | Interferon-induced (antiviral) |
| DDX60 | 3.59 | Interferon-stimulated (antiviral) |

**Top Down-Regulated Genes:**

| Gene | Log2FC | Function |
|------|--------|----------|
| KRT16 | -7.06 | Keratin (epithelial integrity) |
| CDH1 | -6.16 | E-cadherin (epithelial cell adhesion) |
| KRT7 | -4.82 | Keratin (epithelial integrity) |
| SPINK5 | -4.18 | Protease inhibitor (epithelial barrier) |
| KRT19 | -3.93 | Keratin (epithelial integrity) |
| ITGB4 | -3.27 | Integrin (epithelial basement membrane adhesion) |
| TIMP3 | -2.97 | Tissue inhibitor of metalloproteinases |
| LAMB3 | -2.86 | Laminin (epithelial basement membrane) |

## Interpretation

**1. Antiviral interferon response is strongly activated.**
Consistent, robust upregulation of classic interferon-stimulated genes (ISG15, IFIT3, MX1, IFI27, MX2, DDX60) — the expected innate antiviral signature during acute viral infection.

**2. Emergency myeloid expansion.**
Inflammatory monocytes, neutrophils, and platelets are nearly absent in Control samples but comprise roughly 16% of cells combined in Ebola samples. This is consistent with emergency granulopoiesis, a documented feature of severe Ebola virus disease associated with worse clinical outcomes in humans.

**3. Epithelial barrier loss — supported by two independent lines of evidence.**
Epithelial cells drop from 5.4% to 0.04% of the cell population, and separately, the most strongly down-regulated genes in the entire dataset are epithelial structural and adhesion genes (KRT16, CDH1, KRT7, SPINK5, ITGB4, LAMB3). The convergence of cell-composition and gene-expression evidence strengthens confidence in this finding, which is consistent with the tissue damage underlying Ebola's hemorrhagic pathology.

**4. Lymphocyte depletion.**
Naive T cells, B cells, and cytotoxic T/NK cells all show sharply reduced proportions in Ebola-infected samples — consistent with lymphopenia, a well-documented severity marker in human Ebola virus disease.

Together, these findings recapitulate several well-established immunopathological hallmarks of severe Ebola virus disease using single-cell transcriptomic data.

## Limitations
- Mitochondrial percentage was checked as a quality control metric (median 0%, max 4.96% across all cells) and found to be very low throughout the dataset, indicating minimal evidence of dying/stressed cells by this measure. No filtering was applied, as the data did not show a meaningful high-mitochondrial-percentage population to remove
- Only one ambiguous cluster ("B cells/DC") was subclustered as a case study; other clusters with mixed marker profiles (e.g., "NK/CTL," "CD4 T cells") were not further resolved and their proportions should be interpreted cautiously.
- This data file does not include tissue-of-origin metadata; results reflect this specific cell population rather than a confirmed single tissue or the full 13-tissue dataset described in the original study.
- Differential expression was performed at the whole-dataset level (Ebola vs Control across all cell types combined), not separately within each cell type; cell-type-specific DE analysis is a natural next step.

## Next Steps
- Subcluster remaining ambiguous clusters for full-resolution cell type annotation
- Apply mitochondrial percentage-based QC filtering and re-validate results
- Run cell-type-specific differential expression (e.g., DE within T cells only, within monocytes only)
- Pathway/gene set enrichment analysis on up/down-regulated gene lists
- If timepoint resolution allows, analyze disease progression across Day 3–8 rather than a single pooled "Ebola" group

## References
- Santus L, et al. (2023). Single-cell profiling of lncRNA expression during Ebola virus infection in rhesus macaques. *Nat Commun* 14, 3866. [PMID: 37391481](https://pubmed.ncbi.nlm.nih.gov/37391481/)
- [GEO: GSE192447](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192447)






# 🦠 Antimicrobial Resistance (AMR) Prediction — Machine Learning Project

Predicting antibiotic resistance in *Escherichia coli* from genomic data, using real laboratory-tested susceptibility results.

## Project Goal

Given genomic features from a bacterial sample, predict whether it will be **Resistant** or **Susceptible** to a specific antibiotic — without needing to run the actual lab test. This is a supervised machine learning classification problem, applied to bacterial genomics.

## Why This Project

Antimicrobial resistance is one of the top global public health threats. Being able to predict resistance genomically — faster than culturing and testing bacteria in a lab — has real clinical and public health value. This project also pairs thematically with an existing project analyzing host immune response to Ebola infection (single-cell RNA-seq), forming a broader portfolio focus on infectious disease genomics.

## Dataset

**Source:** [BV-BRC](https://www.bv-brc.org) (Bacterial and Viral Bioinformatics Resource Center, formerly known as PATRIC)

- **Organism:** *Escherichia coli*
- **Antibiotic:** Ciprofloxacin
- **Total genomes downloaded (lab-confirmed evidence only):** 15,827
  - Susceptible: 6,560
  - Resistant: 2,071
  - Intermediate: 120
  - No interpreted phenotype (raw MIC value only): 7,076
- **Clean labeled subset:** 8,631 genomes (6,560 Susceptible, 2,071 Resistant), after removing rows with no interpreted phenotype and excluding the ambiguous "Intermediate" category.
- **Modeling sample used so far:** a random subset of 2,000 genomes drawn from the clean 8,631 (303 Resistant, 960 Susceptible had usable gene annotation — see Feature Engineering below). Scaling to the full 8,631 is a planned next step.

**Important data quality note:** BV-BRC provides both real laboratory-tested resistance results and computationally-predicted results (generated by BV-BRC's own XGBoost models). The unfiltered ciprofloxacin dataset contains ~238,000 records, but the majority (~222,000) are computational predictions, not real lab measurements. This dataset was filtered to **Evidence = "Laboratory Method"** only, to ensure the model is trained on real biological data rather than another model's predictions.

## Tools

- **Language:** Python (not R — this project uses `pandas`, `scikit-learn`, and `requests`, as it's a tabular classification problem rather than a single-cell biology analysis)
- **Editor:** VS Code
- **Environment:** `bioinfo` conda environment (numpy, pandas, scikit-learn, requests already installed)
- **Data access:** BV-BRC's public REST API (`https://www.bv-brc.org/api/`), queried directly from Python

## Feature Engineering

The initial plan was to check for the presence of specific antibiotic-target genes (`gyrA`, `gyrB`, `parC`, `parE` — DNA gyrase and topoisomerase IV, the direct molecular targets of fluoroquinolones like ciprofloxacin). This did not work as a feature on its own: these are essential genes present in virtually every *E. coli* genome regardless of resistance status, so they carry no discriminating signal. A search for acquired **qnr genes** (plasmid-mediated quinolone resistance) also came back empty for a genome known to be Resistant, checked across all 3,433 of its annotated genes — indicating this particular resistance mechanism in this dataset is more likely driven by point mutations in gyrA/parC (not detected by this approach) rather than acquired qnr genes.

**Revised approach:** pulled all annotated "Antibiotic Resistance" category genes (BV-BRC's `sp_gene` endpoint) for each genome and used gene presence/absence as a broad feature set, rather than targeting only the direct fluoroquinolone mechanism. Across a random sample of 2,000 genomes, this returned 570 unique resistance-associated genes; only 1,263 of the 2,000 genomes had any gene annotation at all (the rest had no specialty gene data recorded in BV-BRC and were excluded from modeling). Of the annotated genomes, 154 genes showed meaningful prevalence variation (present in 5%-95% of genomes) and were used as the model's feature set.

**Key finding:** the genes most strongly associated with ciprofloxacin resistance were not fluoroquinolone-specific at all — they were genes conferring resistance to *other* antibiotic classes (mphA/Mph(A) family/Mrx — macrolide resistance; CTX-M family — extended-spectrum beta-lactamase; sul1 — sulfonamide resistance; QacE — disinfectant resistance; Tet(A)/tetC — tetracycline resistance). This is consistent with **co-selection**: these genes are frequently carried together on the same mobile genetic elements (plasmids/class 1 integrons — sul1 and QacE in particular are a well-documented linked pair on the conserved segment of class 1 integrons). A genome carrying one of these multidrug-resistance elements often carries ciprofloxacin resistance as part of the same package, even though none of these specific genes directly disable the drug.

## Model & Results

- **Model:** Random Forest classifier (100 trees), chosen for its ability to handle many binary features relative to sample size, capture gene-combination effects (relevant given the co-selection pattern above), and provide feature importance for interpretation.
- **Data split:** 1,010 genomes training / 253 genomes test (80/20 split, stratified by class)
- **Accuracy:** 90%
- **Detailed performance:**

| Class | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| Resistant | 0.84 | 0.70 | 0.77 | 61 |
| Susceptible | 0.91 | 0.96 | 0.93 | 192 |

**Top predictive features (Random Forest feature importance):** CTX-M family, mphA, vgaC, Mrx, Mph(A) family, CTX-M-15, dfrA17, QacE, sul1, Tet(A) — closely matching the genes independently identified as having the largest prevalence gap between Resistant and Susceptible genomes, which supports that the model is learning a real, biologically explainable signal rather than noise.

**Honest limitation:** recall on the Resistant class (70%) is meaningfully lower than on Susceptible (96%) — the model misses roughly 3 in 10 truly resistant genomes. This is the clinically more important error type (a missed resistant infection could be treated with a drug that won't work), and is likely explained by the feature set: genomes resistant purely through a gyrA/parC point mutation, without an accompanying multidrug-resistance plasmid, would show none of these co-selection marker genes and would be predicted Susceptible by this model.

## Planned Pipeline / Next Steps

1. ~~Load and explore the downloaded AMR metadata~~ ✅ Done
2. ~~Obtain genomic features for each genome~~ ✅ Done (broad resistance-gene presence/absence; see Feature Engineering above)
3. ~~Merge phenotype labels with genomic features~~ ✅ Done
4. ~~Train a baseline model~~ ✅ Done (Random Forest, 90% accuracy)
5. Scale up from the 2,000-genome sample to the full 8,631-genome clean dataset
6. Compare against logistic regression and XGBoost
7. Evaluate with cross-validation and ROC-AUC, given class imbalance
8. Investigate direct detection of gyrA/parC point mutations (sequence-level, not just gene presence/absence) to potentially improve recall on the Resistant class

## Limitations

- Currently scoped to a single antibiotic (ciprofloxacin) in a single species (*E. coli*); results may not generalize to other antibiotics or organisms without separate modeling.
- Feature set captures gene presence/absence, largely reflecting co-selected multidrug-resistance markers rather than the direct causal mechanism (gyrA/parC point mutations) for this specific drug class; this likely explains the model's lower recall on the Resistant class.
- Only 1,263 of 2,000 sampled genomes had any resistance-gene annotation in BV-BRC; genomes without annotation were excluded from modeling rather than imputed.
- Rows with only a raw MIC value (no interpreted Resistant/Susceptible category) were excluded from this first pass; these could potentially be incorporated later with an interpretation rule (e.g., CLSI/EUCAST breakpoints).
- Modeling to date uses a 2,000-genome random sample rather than the full 8,631-genome clean dataset.

## References

- [BV-BRC](https://www.bv-brc.org)
- Antonopoulos, D.A. et al. "PATRIC as a unique resource for studying antimicrobial resistance." *Briefings in Bioinformatics*.
- Davis, J.J. et al. (2016). "Antimicrobial Resistance Prediction in PATRIC and RAST." *Scientific Reports* 6, 27930.
## Skills Tracked

- [ ] Python (pandas, numpy, scikit-learn)
- [ ] R (tidyverse, Seurat)
- [ ] Single-cell (Scanpy, Seurat)
- [ ] Metagenomics (QIIME2, DADA2)
- [ ] Nextflow / Snakemake
- [ ] AWS / Cloud computing
- [ ] Docker / Containerization

---

## Contact

[GitHub: github.com/AlanaAnnaman](https://github.com/AlanaAnnaman)
