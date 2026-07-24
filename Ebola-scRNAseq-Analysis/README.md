# Ebola scRNA-seq Analysis

Single-cell RNA-seq analysis of a public dataset from rhesus macaques infected with Ebola virus, examining how immune cell populations and gene expression shift during infection.

## Dataset Summary

| Feature | Details |
|---------|---------|
| **Study** | Santus L, et al. *Nat Commun* 2023 |
| **Organism** | Rhesus macaque (*Macaca mulatta*) |
| **GEO Accession** | [GSE192447](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192447) |
| **Cells analyzed** | 42,881 cells, 16,816 features |
| **Conditions** | Control (pre-infection: Day -30, Day -4, Day 0) vs Ebola-infected (Day 3-8 post-infection) |
| **Control cells** | 7,514 |
| **Ebola cells** | 35,367 |

**Note on scope:** the original study profiled 13 tissues. The specific data file used in this analysis does not include tissue-of-origin metadata, so results here reflect this cell population only, not a confirmed single tissue or the full multi-tissue dataset. This is noted as a limitation below.

## Research Questions
1. How do immune cell populations shift during Ebola infection?
2. What genes and pathways drive the immune response?
3. Can single-cell resolution reveal cell-type-specific effects invisible in bulk analysis?

## Analysis Pipeline
1. Loaded raw expression data (Seurat object)
2. Log-normalized expression data (`NormalizeData`) - required before differential expression; see Data Quality Note below
3. Labeled cells as Control vs Ebola based on sample metadata (day of infection)
4. Identified variable features, scaled data, ran PCA
5. Clustered cells (Louvain algorithm, resolution 0.5) and visualized with UMAP - 18 clusters identified
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
| Naive T cells | 32.2% | 12.6% | Down |
| B cells | 24.6% | 2.3% | Down sharply |
| Cytotoxic T/NK cells | 23.8% | 2.1% | Down sharply |
| Epithelial cells | 5.4% | 0.04% | Down sharply |
| Macrophages | 8.6% | 7.3% | Down slightly |
| Stromal cells | 0.4% | 8.5% | Up |
| Inflammatory monocytes | 0.03% | 6.5% | Up (near-absent in Control) |
| Neutrophils | 0.05% | 5.3% | Up (near-absent in Control) |
| Platelets | 0.05% | 4.2% | Up (near-absent in Control) |
| Activated neutrophils | 0% | 1.4% | Up (absent in Control) |

*Note: initial clusters labeled "B cells/DC," "NK/CTL," and "CD4 T cells" showed large apparent increases in Ebola, but had ambiguous marker profiles suggesting multiple cell types were grouped together (see Subclustering below). These three rows are omitted from the table above pending full resolution.*

## Subclustering: Resolving a Mixed Population

The "B cells/DC" cluster showed a mix of B-cell (MS4A1) and dendritic-cell (CD1C) marker genes, indicating it likely contained more than one true cell type. Re-clustering these ~7,000 cells in isolation split them into 7 sub-populations, including two confidently identifiable types:

- **Naive T cells** - markers: LEF1, ITK, IL7R, FYB1, GIMAP7
- **Cytotoxic NK/CD8 T cells** - markers: GZMB, NKG7, CX3CR1

along with several intermediate lymphocyte activation states and a small contaminating myeloid population. This demonstrates the value of iterative subclustering for resolving cell identity beyond initial coarse clusters.

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

1. **Antiviral interferon response is strongly activated.** Consistent, robust upregulation of classic interferon-stimulated genes - the expected innate antiviral signature during acute viral infection.

2. **Emergency myeloid expansion.** Inflammatory monocytes, neutrophils, and platelets are nearly absent in Control samples but comprise roughly 16% of cells combined in Ebola samples, consistent with emergency granulopoiesis, a documented feature of severe Ebola virus disease.

3. **Epithelial barrier loss, supported by two independent lines of evidence.** Epithelial cells drop from 5.4% to 0.04% of the cell population, and separately, the most strongly down-regulated genes are epithelial structural and adhesion genes - consistent with the tissue damage underlying Ebola's hemorrhagic pathology.

4. **Lymphocyte depletion.** Naive T cells, B cells, and cytotoxic T/NK cells all show sharply reduced proportions in Ebola-infected samples, consistent with lymphopenia, a well-documented severity marker in human Ebola virus disease.

Together, these findings recapitulate several well-established immunopathological hallmarks of severe Ebola virus disease using single-cell transcriptomic data.

## Limitations

- Mitochondrial percentage was checked as a quality control metric (median 0%, max 4.96% across all cells) and found to be very low throughout the dataset. No filtering was applied, as there was no meaningful high-mitochondrial-percentage population to remove.
- Only one ambiguous cluster ("B cells/DC") was subclustered as a case study; other clusters with mixed marker profiles were not further resolved.
- This data file does not include tissue-of-origin metadata; results reflect this specific cell population rather than a confirmed single tissue or the full 13-tissue dataset described in the original study.
- Differential expression was performed at the whole-dataset level, not separately within each cell type; cell-type-specific DE analysis is a natural next step.

## Next Steps

- Subcluster remaining ambiguous clusters for full-resolution cell type annotation
- Run cell-type-specific differential expression (e.g., DE within T cells only, within monocytes only)
- Pathway/gene set enrichment analysis on up/down-regulated gene lists
- If timepoint resolution allows, analyze disease progression across Day 3-8 rather than a single pooled "Ebola" group

## References

- Santus L, et al. (2023). Single-cell profiling of lncRNA expression during Ebola virus infection in rhesus macaques. *Nat Commun* 14, 3866. [PMID: 37391481](https://pubmed.ncbi.nlm.nih.gov/37391481/)
- [GEO: GSE192447](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192447)
