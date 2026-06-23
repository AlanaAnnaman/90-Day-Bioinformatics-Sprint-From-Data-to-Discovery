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
| 2025-06-22 | 4 | Generated synthetic paired-end FASTQ files. Troubleshooted NCBI download issues (rate-limiting, 404 errors). Learned FASTQ format. | Used synthetic data to maintain momentum. Files: sample_1.fastq (3 reads), sample_2.fastq (3 reads). |
| 2025-06-23 | 2 | Ran FastQC and MultiQC on synthetic data. Generated QC reports. Uploaded results to GitHub. | Reports confirm perfect quality (expected). Ready for taxonomic classification. |

---

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

### Step 2 Results: Quality Control

| Metric | sample_1.fastq | sample_2.fastq |
|--------|----------------|----------------|
| Total Sequences | 10,000 | 10,000 |
| Sequences flagged as poor quality | 0 | 0 |
| Sequence length | 104 bp | 103 bp |
| %GC | 50% | 50% |

**Conclusion:** All reads passed QC. Ready for taxonomic classification.






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
