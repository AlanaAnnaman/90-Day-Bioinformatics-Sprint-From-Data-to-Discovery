# PAH Gene Mutation Project: Predicting Whether a Genetic Variant Is Harmful

## Overview

Phenylketonuria (PKU) is a hereditary metabolic condition in which the body is unable to properly break down an amino acid called phenylalanine. Left untreated, this buildup can cause serious neurological damage. PKU is caused by mutations in a single gene, called PAH.

A gene can be thought of as a set of instructions written in a four letter genetic alphabet. A mutation is a small change somewhere in that sequence. Some mutations have no meaningful effect, while others disrupt the resulting protein enough to cause disease.

This project asks the same practical question as an earlier project on Familial Mediterranean Fever: given a PAH mutation, can a model predict whether it is likely to be harmful or harmless, based only on the mutation's own properties?

## Motivation

Turkiye has one of the highest documented rates of PKU in the world. This is closely tied to a broader pattern: Turkiye also has a comparatively high rate of consanguineous marriage (marriage between close relatives, most often first cousins), and PKU is a recessive condition, meaning a child only develops it if they inherit a harmful copy of the gene from both parents. Related parents are more likely to carry the same rare mutation, which raises the chance of this outcome. This project extends a broader personal interest in genetic mutations and their real-world consequences, building on prior work analyzing infectious disease genomics and other single-gene conditions.

## Data Source

Data was obtained from ClinVar, a public archive of expert-reviewed genetic variant classifications maintained by the National Center for Biotechnology Information (NCBI). ClinVar was chosen specifically because it provides clinical significance classifications (whether a variant is considered harmful or harmless), rather than only raw sequence data, which is what several other major bioinformatics databases (GenBank, SRA, UniProt, and organism-specific databases) provide instead.

ClinVar's full variant summary file covers millions of variants across every human gene. Because of its size, the file was read in smaller chunks (100,000 rows at a time) rather than loaded into memory all at once, filtering for PAH gene variants as each chunk was processed. This returned 3,420 PAH-related variants in total.

Of these, 2,639 had a clear classification after cleaning: 1,810 Pathogenic and 829 Benign. Variants labeled "Uncertain significance," "Conflicting classifications of pathogenicity," "not provided," or without any classification were excluded, since they do not represent a confident answer to learn from. Compound labels such as "Pathogenic/Likely pathogenic" and "Benign/Likely benign" were retained and merged into their base category, since both halves of each label agree on the same underlying direction (harmful or harmless), differing only in the reviewing lab's stated confidence.

Two features of this cleaned dataset are worth noting. First, only 19.5 percent of PAH variants were classified as "Uncertain significance," a notably lower share than has been observed in more narrowly studied genes, consistent with PKU's status as an extensively researched and widely screened condition. Second, Pathogenic variants make up the majority of the cleaned dataset (69 percent), which is unlikely to reflect the true balance of harmful versus harmless PAH variants in the general population. This is more plausibly explained by ascertainment bias: genetic testing is typically ordered because a patient is already suspected of having a condition, so databases like ClinVar are likely to overrepresent disease-causing variants relative to how common they actually are in a random, healthy person's genome.

## Identifying Useful Features

Two properties of each mutation were evaluated as potential predictors.

The general type of mutation was considered first, such as a single nucleotide substitution versus a larger deletion or duplication. Single nucleotide variants accounted for the large majority of mutations in both categories (76.5 percent of Pathogenic variants and 96.6 percent of Benign variants), leaving limited variation to distinguish the two groups. One meaningful difference did emerge: deletions were substantially more common among Pathogenic variants (15.5 percent) than Benign variants (2.4 percent), consistent with the expectation that removing genetic material is more likely to disrupt the reading frame of the resulting protein than a single letter substitution.

The location of each mutation within the gene was also considered, using a marker in the variant's formal notation that indicates whether a mutation falls after the gene's coding region. This marker was present in only 2 of 2,639 variants and could not be used, most likely because variants in this region were disproportionately classified as "Uncertain significance" and were therefore removed during the earlier cleaning step.

The specific base substitution involved in each mutation, for example a C changing to a T, was evaluated next. This information was extracted from the variant's formal notation using pattern matching, since it was not available as its own column. Substitution type showed genuine variation between the two classes; for example, C-to-T and T-to-C changes were both notably more common among Benign variants, while G-to-C and G-to-T changes were more common among Pathogenic variants.

The final feature set consisted of two properties: the general type of mutation, and the specific base substitution involved, both represented as separate indicator columns.

## Model and Results

A Random Forest classifier was trained on 80 percent of the dataset and evaluated on the remaining 20 percent.

Using mutation type alone, the model achieved 68.6 percent accuracy. This figure is misleading on its own: it corresponds almost exactly to the proportion of Pathogenic variants in the dataset, and the model in fact predicted "Pathogenic" for every case in the test set, correctly identifying 0 percent of the truly Benign variants.

An initial attempt to correct this using class weighting, giving equal importance to both categories rather than allowing the majority class to dominate, overcorrected substantially. Benign recall rose to 96 percent, but Pathogenic recall fell to 21 percent, and overall accuracy dropped to 44 percent, performing worse than chance.

Adding the base substitution feature alongside mutation type, without class weighting, produced a more modest but genuine improvement. Benign recall rose from 0 percent to 15 percent, with 50 percent precision on Benign predictions, while Pathogenic recall remained high (93 percent). Overall accuracy remained essentially unchanged (68.6 percent), since gains on the minority class have limited effect on an aggregate metric when that class is comparatively small.

| Feature Set | Accuracy | Benign Recall | Benign Precision |
|---|---|---|---|
| Mutation type only | 68.6% | 0% | undefined (no predictions made) |
| Mutation type, class-weighted | 44.3% | 96% | 36% |
| Mutation type + base substitution | 68.6% | 15% | 50% |

## Interpretation

Of the two feature-based approaches attempted, using mutation type combined with base substitution produced the most balanced outcome, improving the model's ability to identify Benign variants without the severe accuracy collapse seen under class weighting. Even so, the improvement is modest: the model still fails to identify the large majority of truly Benign variants. This indicates that mutation type and base substitution, while genuinely informative, are not sufficient on their own to reliably distinguish harmful from harmless PAH variants. This is an honest and legitimate finding rather than a failed outcome; it suggests that a stronger model would likely require additional information not readily available in this dataset, such as the mutation's predicted effect on protein structure or evolutionary conservation at the affected position.

## Future Directions

Incorporating protein-level features, such as which functional domain of the PAH protein is affected, or computational conservation scores, would likely improve model performance. Applying this same approach to other genes associated with conditions common in populations with high consanguinity rates would also help establish how well these findings generalize.

## Data Source

ClinVar (NCBI): https://www.ncbi.nlm.nih.gov/clinvar/
