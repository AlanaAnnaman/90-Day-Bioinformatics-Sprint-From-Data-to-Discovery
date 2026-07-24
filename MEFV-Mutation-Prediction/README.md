# MEFV Mutation Project: Predicting Whether a Genetic Variant Is Harmful

## Overview

Familial Mediterranean Fever is a hereditary condition that causes repeated episodes of fever and abdominal pain. It is especially common in people of Turkish, Armenian, Arab, or Jewish descent, and it is caused by a mutation in a single gene, called MEFV.

A gene can be thought of as a set of instructions written in a four letter genetic alphabet. Most people's copy of a given gene reads the same way. A mutation is a small change somewhere in that copy. Some mutations have no real effect, similar to a typo in a page margin nobody reads. Others disrupt something important enough to cause disease.

This project set out to answer a practical question: given a MEFV mutation, can a model predict whether it is likely to be harmful or harmless, based only on the mutation's own properties? This is a genuine, ongoing challenge in clinical genetics. When a new mutation is identified in a patient, it is often unclear at first whether it should be treated as a concern.

## Motivation

This project extends an existing portfolio built around infectious disease genomics, including an Ebola immune response analysis and an antimicrobial resistance prediction model. It also reflects a personal interest in understanding what distinguishes a harmful genetic mutation from a harmless one, and connects naturally to Turkiye, where Familial Mediterranean Fever is particularly prevalent.

## Data Source

Data was obtained from INFEVERS, a public database of autoinflammatory disease mutations maintained by the International Society for Systemic Autoinflammatory Diseases (https://infevers.umai-montpellier.fr).

Of the records available for the MEFV gene, 205 mutations had a clear, expert-reviewed classification. Of these, 157 were classified as Benign and 48 as Pathogenic. Records classified as "Uncertain significance" or left unresolved were excluded, since they do not represent a confident answer to learn from.

## Identifying Useful Features

Several properties of each mutation were evaluated as potential predictors.

The protein level effect of each mutation was considered first, but this information was missing for the large majority of records and could not be used.

The general type of mutation, such as a single letter substitution versus a larger deletion, was also considered. However, 96 percent of all mutations in the dataset were simple substitutions, leaving little variation to distinguish harmful from harmless cases.

The location of each mutation within the gene proved more informative. Genes contain coding regions, known as exons, which directly determine the structure of the resulting protein, and non-coding regions, known as introns, which are typically removed before the protein is built. Pathogenic mutations were found in exons 96 percent of the time, compared to 80 percent for benign mutations, a meaningful difference consistent with known biology.

The specific base substitution involved in each mutation, for example a C changing to a T, showed sufficient variation across the dataset to serve as an additional feature.

The final feature set therefore consisted of two properties: the region of the gene in which the mutation occurs, and the specific base substitution involved.

## Model and Results

A Random Forest classifier was trained on 80 percent of the dataset and evaluated on the remaining 20 percent.

The initial model achieved 83 percent accuracy. This figure warrants some context: because benign mutations make up the majority of the dataset, a model that simply predicted "benign" for every case would already achieve approximately 76 percent accuracy without using any information at all. The more meaningful measure of performance is how well the model identifies mutations that are genuinely pathogenic. Of 10 truly pathogenic mutations in the test set, the model correctly identified only 3.

A second version of the model was trained with class weighting adjusted to give equal importance to both categories, rather than allowing the more common category to dominate. This version correctly identified 5 of the 10 pathogenic mutations, an improvement in sensitivity. However, overall accuracy fell to 56 percent, as the model began misclassifying a substantial number of benign mutations as pathogenic.

| Model Version | Accuracy | Pathogenic Cases Correctly Identified |
|---|---|---|
| Standard | 83% | 3 of 10 |
| Class-weighted | 56% | 5 of 10 |

Neither version is unambiguously superior. The standard model is highly reliable whenever it flags a mutation as pathogenic, but misses most true positive cases. The class-weighted model identifies more true positives, at the cost of a substantially higher false positive rate. In a clinical context, where failing to flag a genuinely harmful mutation may carry greater risk than a false alarm, this tradeoff has real practical significance and does not resolve to a single "best" answer.

## Interpretation

With only 205 labeled examples and two relatively simple features, this dataset offers limited information relative to, for example, the several thousand genomes used in the accompanying antimicrobial resistance project. That a real, biologically coherent signal was identified under these constraints, namely that pathogenic mutations cluster in coding regions, is a meaningful finding in its own right. Reporting the accuracy tradeoff transparently, rather than presenting a single favorable metric, reflects a more accurate and appropriately cautious account of the model's actual performance.

## Biological Context

The MEFV gene encodes a protein called pyrin, which functions within certain immune cells as part of the body's inflammatory response system. Under normal conditions, pyrin helps trigger inflammation, such as fever, in response to genuine threats like infection.

A pathogenic mutation alters pyrin's structure sufficiently to disrupt this regulation, causing the inflammatory response to activate without a genuine trigger, or to fail to deactivate appropriately. This produces the recurrent fever episodes characteristic of Familial Mediterranean Fever.

This also explains why mutation location was found to be predictive. A mutation within an exon can directly alter the structure of the pyrin protein, while a mutation within an intron is typically removed before the protein is constructed and therefore has little effect on its final structure. This is consistent with the higher concentration of pathogenic mutations observed in exons.

## Future Directions

Incorporating additional features, such as protein-level conservation scores or existing computational prediction tools, would likely improve model performance. Applying this same approach to a larger set of mutations, potentially across additional genes represented in the INFEVERS database, would also help establish how well these findings generalize beyond this initial, modestly sized dataset.

## Data Source

INFEVERS: https://infevers.umai-montpellier.fr
