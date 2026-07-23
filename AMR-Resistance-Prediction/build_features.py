# ============================================================
# ML WORKFLOW OVERVIEW - Antimicrobial Resistance (AMR) Prediction Project
# ============================================================
# 1. Define the problem                                                          [DONE]
# 2. Collect data                                                                [DONE - see collect_data.py]
# 3. Clean and prepare the data                                                  [DONE - see collect_data.py]
# 4. Feature engineering                                                         [DONE - this file]
# 5. Split the data into training and test sets                                  [DONE - this file]
# 6. Choose a model: compared Logistic Regression, Random Forest, XGBoost        [DONE - this file]
# 7. Train the model                                                             [DONE - this file]
# 8. Evaluate the model: accuracy 90%, 5-fold cross-validation average 90.7%     [DONE - this file]
#    (+/- 2.4%), ROC-AUC 0.92
# 9. Interpret the results: top predictive genes matched an independent          [DONE - this file]
#    statistical comparison of gene prevalence between classes - the model
#    learned real, biologically explainable signal (co-selection on shared
#    multidrug-resistance plasmids), not noise
# 10. Iterate/improve: compared 3 models (similar performance -> feature set,    [DONE - this file]
#     not algorithm, is the current ceiling); found and fixed a class-order bug
#     in the ROC-AUC calculation
#     NEXT STEP (future work): direct detection of gyrA/parC point mutations at
#     the sequence level - this dataset's resistance appears to be driven more
#     by point mutations than acquired qnr genes, which may improve recall on
#     the Resistant class (currently 72%)
# ============================================================


# ============================================================
# STEP 4 (continued): Build gene presence/absence feature columns
# Turns the raw gene lists (collected in collect_data.py) into a proper table
# a model can use - one column per gene, 1 = present, 0 = absent
# ============================================================
import pandas as pd

df = pd.read_csv("genome_resistance_genes_2000.csv")

# Some genomes had no genes returned (blank) - fill those with empty string
df["resistance_genes"] = df["resistance_genes"].fillna("")

# Split "geneA;geneB;geneC" into an actual Python list: [geneA, geneB, geneC]
df["gene_list"] = df["resistance_genes"].apply(lambda x: x.split(";") if x else [])

# Collect every unique gene name that appears anywhere across all genomes
all_genes = set()
for genes in df["gene_list"]:
    all_genes.update(genes)
all_genes.discard("")

print(f"Total unique genes found across all genomes: {len(all_genes)}")

# Build all gene columns at once (1 = gene present, 0 = absent) - faster than
# looping one column at a time, which triggers a pandas performance warning
gene_columns = pd.DataFrame({
    gene: df["gene_list"].apply(lambda genes: 1 if gene in genes else 0)
    for gene in all_genes
})

df = pd.concat([df, gene_columns], axis=1)

df.to_csv("amr_feature_table.csv", index=False)
print("Saved feature table with shape:", df.shape)
print(df.head())


# ============================================================
# STEP 4 (continued): Data quality check
# Some genomes had NO gene annotation at all in BV-BRC - need to find and set
# these aside, since an all-zero row gives a model nothing to learn from
# ============================================================
df_model = df.drop(columns=["resistance_genes", "gene_list"])  # drop text columns, not usable by a model

genes_only = df_model.drop(columns=["Genome ID", "Resistant Phenotype"])
print("Genomes with at least one gene detected:", (genes_only.sum(axis=1) > 0).sum(), "out of", len(df_model))

# Check how common each gene is across genomes - a gene present in almost
# everyone (or almost no one) can't help distinguish Resistant vs Susceptible.
# This confirmed gyrA/gyrB/parC/parE (ciprofloxacin's direct targets) are
# near-universal and therefore useless as standalone features.
gene_frequency = genes_only.sum(axis=0).sort_values(ascending=False)
print("\nTop 15 most common genes:")
print(gene_frequency.head(15))


# ============================================================
# STEP 4 (continued): Feature engineering - keep only genomes and genes that
# are actually useful for modeling
# ============================================================
# Drop the ~737 genomes with zero gene data - they'd just be blank rows with
# nothing to learn from
annotated = df_model[genes_only.sum(axis=1) > 0].copy()
print("Genomes with annotation:", len(annotated))

annotated_genes_only = annotated.drop(columns=["Genome ID", "Resistant Phenotype"])

# Keep only genes present in 5%-95% of genomes (excludes "everyone has it" and
# "almost no one has it" genes, since neither type carries a useful predictive
# signal). This narrows 570 genes down to 154 with meaningful variation.
gene_freq_pct = annotated_genes_only.mean(axis=0)  # mean of 0/1 values = % of genomes with that gene
useful_genes = gene_freq_pct[(gene_freq_pct >= 0.05) & (gene_freq_pct <= 0.95)].index.tolist()

print(f"\nGenes with meaningful variation (5%-95% prevalence): {len(useful_genes)}")
print(gene_freq_pct[useful_genes].sort_values(ascending=False).head(20))


# ============================================================
# STEP 4 (continued): Check WHICH genes actually differ between Resistant and
# Susceptible (having variation isn't enough - it needs to vary WITH the
# outcome we care about, not just vary randomly)
# ============================================================
resistant_genomes = annotated[annotated["Resistant Phenotype"] == "Resistant"]
susceptible_genomes = annotated[annotated["Resistant Phenotype"] == "Susceptible"]

resistant_freq = resistant_genomes[useful_genes].mean(axis=0)
susceptible_freq = susceptible_genomes[useful_genes].mean(axis=0)

comparison = pd.DataFrame({
    "Resistant_pct": resistant_freq,
    "Susceptible_pct": susceptible_freq,
    "difference": resistant_freq - susceptible_freq
}).sort_values("difference", ascending=False)

print("Genomes - Resistant:", len(resistant_genomes), "| Susceptible:", len(susceptible_genomes))
print("\nTop 15 genes MORE common in Resistant genomes:")
print(comparison.head(15))
# Result: top genes (mphA, CTX-M family, sul1, QacE, Tet(A), etc.) are markers
# of OTHER antibiotic classes, not ciprofloxacin-specific - consistent with
# co-selection on shared multidrug-resistance plasmids/integrons (sul1+QacE in
# particular is a documented linked pair on class 1 integrons)

print("\nTop 15 genes MORE common in Susceptible genomes:")
print(comparison.tail(15))


# ============================================================
# STEP 5: Split the data into training and test sets
# Training set = what the model learns from. Test set = held back, used to
# check performance afterward on data the model has never seen.
# ============================================================
from sklearn.model_selection import train_test_split

X = annotated[useful_genes]              # features (which genes are present)
y = annotated["Resistant Phenotype"]     # label (the answer we want to predict)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)  # 80% train / 20% test, keeping the same Resistant:Susceptible ratio in both

print("Training set size:", X_train.shape)
print("Test set size:", X_test.shape)


# ============================================================
# STEP 6-7: Choose a model (Random Forest as the primary/baseline model) and train it
# Random Forest chosen for: handling many binary features relative to sample
# size, capturing gene-combination effects (relevant given the co-selection
# pattern found above), and providing feature importance for interpretation.
# ============================================================
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)  # 100 decision trees, voting together
model.fit(X_train, y_train)  # this is the actual "learning" step

print("Model trained successfully.")


# ============================================================
# STEP 8: Evaluate the model on the held-out test set
# ============================================================
from sklearn.metrics import accuracy_score, classification_report

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nDetailed report:\n", classification_report(y_test, predictions))
# Result: ~90% accuracy. Precision/recall strong for Susceptible (0.92/0.96)
# but notably weaker for Resistant (0.85/0.72) - the model misses roughly 3 in
# 10 truly resistant genomes, likely those relying on an undetected gyrA/parC
# point mutation rather than a co-selected marker gene.


# ============================================================
# STEP 9: Interpret the results - which genes did the model rely on most?
# ============================================================
importances = pd.Series(model.feature_importances_, index=X.columns)
top_features = importances.sort_values(ascending=False).head(15)

print("\nTop 15 most important genes for predicting resistance:")
print(top_features)
# Result: top features (CTX-M family, mphA, vgaC, Mrx, dfrA17, QacE, sul1)
# closely match the genes independently flagged in the prevalence comparison
# above - confirms the model learned real, explainable biology, not noise.


# ============================================================
# STEP 6 (comparison) / STEP 10 (iterate): Try two more models on the exact
# same data/split, to see if a different algorithm performs meaningfully better
# ============================================================
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

# --- Logistic Regression: simplest model, treats each gene's effect independently ---
log_model = LogisticRegression(max_iter=1000, random_state=42)
log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)

print("=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, log_preds))
print(classification_report(y_test, log_preds))

# --- XGBoost: builds trees one at a time, each one fixing the previous one's mistakes ---
# XGBoost requires numeric labels (0/1) instead of text
y_train_numeric = y_train.map({"Susceptible": 0, "Resistant": 1})
y_test_numeric = y_test.map({"Susceptible": 0, "Resistant": 1})

xgb_model = XGBClassifier(random_state=42, eval_metric="logloss")
xgb_model.fit(X_train, y_train_numeric)
xgb_preds = xgb_model.predict(X_test)

print("\n=== XGBoost ===")
print("Accuracy:", accuracy_score(y_test_numeric, xgb_preds))
print(classification_report(y_test_numeric, xgb_preds))

# Result: all three models land within ~2 percentage points of each other
# (88-90% accuracy). This indicates the current FEATURE SET, not the choice of
# algorithm, is the limiting factor - a meaningful finding in itself.
# Logistic Regression notably has the lowest Resistant recall (0.64 vs
# 0.70-0.72), likely because it can't capture gene-combination effects
# (e.g. sul1+QacE co-occurring) the way tree-based models can.


# ============================================================
# Visualize the 3-model comparison (Random Forest vs Logistic Regression vs XGBoost)
# ============================================================
import matplotlib.pyplot as plt

# Results typed in manually from the runs above, just to make the charts
models = ["Random Forest", "Logistic Regression", "XGBoost"]
accuracy = [0.901, 0.881, 0.897]
resistant_precision = [0.85, 0.83, 0.84]
resistant_recall = [0.72, 0.64, 0.70]
resistant_f1 = [0.78, 0.72, 0.77]

# Chart 1: overall accuracy, side by side
plt.figure(figsize=(6, 4))
plt.bar(models, accuracy, color=["#4C72B0", "#DD8452", "#55A868"])
plt.ylim(0.7, 1.0)
plt.ylabel("Accuracy")
plt.title("Overall Accuracy by Model")
for i, v in enumerate(accuracy):
    plt.text(i, v + 0.01, f"{v:.1%}", ha="center")
plt.tight_layout()
plt.savefig("model_accuracy_comparison.png", dpi=150)
plt.show()

# Chart 2: precision/recall/F1 specifically for the Resistant class
# (this is where the differences between models actually show up)
x = range(len(models))
width = 0.25

plt.figure(figsize=(7, 5))
plt.bar([i - width for i in x], resistant_precision, width, label="Precision")
plt.bar(x, resistant_recall, width, label="Recall")
plt.bar([i + width for i in x], resistant_f1, width, label="F1-score")

plt.xticks(x, models)
plt.ylim(0, 1.0)
plt.ylabel("Score")
plt.title("Resistant-Class Performance by Model")
plt.legend()
plt.tight_layout()
plt.savefig("resistant_class_comparison.png", dpi=150)
plt.show()

print("Charts saved: model_accuracy_comparison.png and resistant_class_comparison.png")


# ============================================================
# STEP 8 (continued): More rigorous evaluation - cross-validation and ROC-AUC
# Checks whether the 90% accuracy is stable/trustworthy, not just a lucky
# single train/test split
# ============================================================
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score

# Cross-validation: split the data 5 different ways, train/test 5 times, and
# average the results
cv_scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print("Cross-validation accuracy scores (5 folds):", cv_scores)
print("Average accuracy:", cv_scores.mean(), "+/-", cv_scores.std())
# Result: average 90.7% (+/- 2.4%), consistent with the single-split accuracy
# above - confirms the result is stable, not a lucky split.

# ROC-AUC: a single score measuring how well the model separates Resistant vs
# Susceptible overall (1.0 = perfect separation, 0.5 = no better than random
# guessing). IMPORTANT: model.classes_ order isn't guaranteed to put
# "Resistant" in column 1 - look it up explicitly to avoid an inverted score.
print("Class order:", model.classes_)

y_test_binary = y_test.map({"Susceptible": 0, "Resistant": 1})
resistant_col_index = list(model.classes_).index("Resistant")
y_probs = model.predict_proba(X_test)[:, resistant_col_index]

auc_score = roc_auc_score(y_test_binary, y_probs)
print("\nROC-AUC score:", auc_score)
# Result: 0.92 - strong separation between classes, consistent with the other
# metrics above. (An earlier version of this code assumed column index 1 was
# always "Resistant" without checking, which produced an inverted/invalid
# score of ~0.08 - fixed by looking up the correct index via model.classes_.)
