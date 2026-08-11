# Gut Microbiome in Moroccan COVID-19 Patients: A 16S rRNA Analysis

## Overview

This project analyzes gut microbiome composition in hospitalized COVID-19 patients versus healthy controls in Morocco, using 16S rRNA amplicon sequencing data. It asks a two-part question: does having COVID-19 change the composition of gut bacteria, and does the antibiotic treatment these patients received (azithromycin) compound that effect?

## Motivation

This project extends an ongoing interest in how infection and treatment reshape the human microbiome, building on prior work in infectious disease genomics (Ebola immune response) and antimicrobial resistance prediction. It also connects to a broader personal interest in country-specific health data, in this case Morocco.

## Dataset

**Source:** NCBI Sequence Read Archive, BioProject [PRJNA728736](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA728736)

**Study:** 16S rRNA gene amplicon taxonomic profiling of hospitalized Moroccan COVID-19 patients, published in *Microbiology Resource Announcements* (2022), collected at a hospital in Casablanca, Morocco.

- **8 total samples:** 4 hospitalized COVID-19 patients (treated with azithromycin) and 4 healthy controls
- Sample-to-group mapping was inferred from the order SRX accessions were listed in the source paper and confirmed to resolve to sequential SRR run numbers in the same order; this was not independently cross-verified against NCBI's own per-sample metadata due to a connectivity issue with NCBI's E-utilities during analysis, and should be treated as a reasonable but unconfirmed assumption.

## Tools

- **Data retrieval:** SRA Toolkit (`prefetch`, `fasterq-dump`)
- **Pipeline:** QIIME2 (2026.7 "rachis-qiime2" release), run via a dedicated conda/micromamba environment on Apple Silicon (Rosetta 2 emulation, as native ARM builds are not yet available)
- **Reference database:** SILVA 138 99% full-length classifier

## Pipeline

1. Downloaded 8 samples from NCBI SRA and converted to paired-end FASTQ format
2. Built a QIIME2 manifest and imported data as `SampleData[PairedEndSequencesWithQuality]`
3. Assessed read quality; truncated forward reads to 270bp and reverse reads to 220bp based on quality score decay
4. Denoised with DADA2 (multi-threaded) to generate a feature table and representative sequences
5. Assigned taxonomy using a SILVA 138 naive Bayes classifier
6. Built a phylogenetic tree (MAFFT alignment + FastTree)
7. Calculated alpha diversity (Shannon, Observed Features, Faith's Phylogenetic Diversity) and beta diversity (weighted/unweighted UniFrac, Bray-Curtis, Jaccard) at a rarefaction depth of 3,000 sequences per sample
8. Tested for significant differences between COVID-19 and Control groups (Kruskal-Wallis for alpha diversity, PERMANOVA for beta diversity)
9. Collapsed data to genus level and ran ANCOM-BC differential abundance testing between groups

## Data Quality Notes

Two real technical issues arose during this analysis and are documented here for transparency, since they affected intermediate results before being resolved:

**Read merging failure on first DADA2 attempt.** An initial truncation length (240bp forward, 200bp reverse) left insufficient overlap between paired reads, resulting in a catastrophic merge failure (0-3% of reads successfully merged per sample, versus a healthy 60-90%+ expected). This was diagnosed by inspecting the DADA2 denoising statistics table and resolved by increasing truncation lengths to 270bp/220bp, which restored merge rates to 73-80% across all samples.

**Taxonomy classifier version incompatibility.** The initially downloaded SILVA classifier was trained with an older scikit-learn version (0.24.1) incompatible with the current QIIME2 release's bundled scikit-learn (1.7.1). This was resolved by downgrading scikit-learn to 1.4.2 within the QIIME2 environment and downloading a classifier trained with a matching version.

**Elevated chimera removal rate.** Following the corrected DADA2 run, 80-93% of merged reads were flagged and removed as chimeric sequences, notably higher than the typical 5-20% range. This most likely reflects properties of the original PCR amplification in the source study rather than an error in this analysis, and is noted as a limitation. Despite this, all 8 samples retained a workable number of final sequences (6,500-20,000+ per sample).

## Results

### Alpha Diversity (diversity within each sample)

| Metric | p-value | Significant? |
|---|---|---|
| Shannon diversity | 0.564 | No |
| Observed features | 0.773 | No |
| Faith's phylogenetic diversity | 0.149 | No |

No alpha diversity metric showed a statistically significant difference between COVID-19 and Control groups. Overall bacterial diversity within individual samples does not appear to differ meaningfully between groups.

### Beta Diversity (differences between samples)

Weighted UniFrac PERMANOVA: **p = 0.055** — did not reach conventional statistical significance (p < 0.05), but was close to the threshold despite the small sample size.

A PCoA plot of weighted UniFrac distances showed visible separation between COVID-19 and Control samples along the first principal coordinate axis (51.36% of variance explained), with COVID-19 samples clustering toward one end and Control samples toward the other, though with some overlap and at least one outlier in each group.

### Differential Abundance (genus level)

Of 224 bacterial genera tested, 3 showed a statistically significant difference between groups (q < 0.05, ANCOM-BC):

| Genus | Log-fold-change | q-value | Direction |
|---|---|---|---|
| UBA1819 (family Ruminococcaceae) | -3.23 | 0.0014 | Higher in COVID-19 |
| *Butyricimonas* | -3.44 | 0.0021 | Higher in COVID-19 |
| Uncultured genus | +1.91 | 0.0325 | Higher in Control |

*Butyricimonas* is a known butyrate-producing genus; butyrate is generally associated with gut barrier health and anti-inflammatory effects, making its elevation in COVID-19 patients a genuinely interesting, if not fully explained, finding rather than a straightforward "more beneficial bacteria" story. UBA1819 is a poorly characterized genus with limited existing functional literature. The third genus is uncultured and its function is unknown.

## Interpretation

Overall bacterial diversity does not differ significantly between hospitalized Moroccan COVID-19 patients and healthy controls in this dataset, but overall community composition shows a borderline-significant difference (p = 0.055) that is visually apparent in ordination space. At the individual genus level, a small number of specific taxa, most notably *Butyricimonas* and UBA1819, differ significantly between groups. Together, this suggests the COVID-19/antibiotic-treatment effect on the gut microbiome in this dataset is targeted rather than a broad, sweeping community-wide shift, though this interpretation should be treated as exploratory given the sample size.

## Limitations

- Sample size is very small (4 COVID-19, 4 Control), limiting statistical power; the borderline beta diversity result (p = 0.055) would benefit from replication in a larger cohort.
- COVID-19 patients in this dataset were also treated with azithromycin; this analysis cannot separate the effect of viral infection from the effect of antibiotic treatment, since both differ simultaneously between groups.
- Sample group assignment (COVID-19 vs. Control) was inferred from the order of accessions in the source publication and could not be independently cross-verified against NCBI's own per-sample metadata due to a tool connectivity issue during analysis.
- 16S rRNA sequencing profiles a single marker gene and cannot resolve species-level identity as precisely as shotgun metagenomic sequencing, and does not provide direct functional (gene-level) information.
- Chimera removal rates were higher than typical, likely reflecting the original study's PCR conditions rather than an artifact of this analysis, but this reduces the effective sequencing depth retained per sample.

## References

- Original study: Gut Microbiome 16S rRNA Gene Amplicon Taxonomic Profiling of Hospitalized Moroccan COVID-19 Patients. *Microbiology Resource Announcements*, 2022.
- BioProject: [PRJNA728736](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA728736)
- QIIME2: Bolyen et al. (2019), *Nature Biotechnology*
- SILVA reference database: Quast et al. (2013), *Nucleic Acids Research*
