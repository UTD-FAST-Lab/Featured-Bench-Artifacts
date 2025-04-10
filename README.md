# The Artifacts for Program Feature-based Benchmarking for FuzzTesting

## Table of Contents

- [The Artifacts for Program Feature-based Benchmarking for FuzzTesting](#the-artifacts-for-program-feature-based-benchmarking-for-fuzztesting)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [Provenance](#provenance)
  - [Data](#data)
    - [RQ1](#rq1)
    - [RQ2](#rq2)
  - [Setup](#setup)
    - [Requirements](#requirements)
    - [Instructions](#instructions)
  - [Usage](#usage)
    - [Basic Usage Example](#basic-usage-example)
      - [Detecting Nondeterminism Using Strategy I](#detecting-nondeterminism-using-strategy-i)
      - [How to Read Output](#how-to-read-output)
      - [Detecting Nondeterminism Using Strategy II](#detecting-nondeterminism-using-strategy-ii)
      - [Post-processing Results](#post-processing-results)
    - [Replicating Major Paper Results](#replicating-major-paper-results)

## Purpose

This artifact contains the FeatureBench, code and data for the paper titled ***"Program Feature-based Benchmarking for FuzzTesting"***.

The `FeatureBench` directory contains the benchmark programs generated from this work.

The `code` directory contains the source code of the benchmark generation scripts used in Section 4 and the experiment scripts used in Section 5. 

The `data` directory contains the experimental data, and visualizations (heatmaps) that support the conclusions made in the two research questions (RQ1 and RQ2). 

We are applying for the **Available**, **Functional**, and **Reusable** badges.

We believe we deserve the **Available** badge because our artifact is available on Zenodo at https://doi.org/xxxxxxxx (DOI xxxxxx/zenodo.xxxxx) for long-term archiving.

We believe we deserve the **Functional** and **Reusable** badges because our artifact can be executed and used to generate the benchmark programs and experimental results as described in the paper.
Our README.md file gives guidance on how to setup and run the experiments in our paper. 

## Provenance

The artifact as reported in the original paper is available on Zenodo
(https://doi.org/xxxxxxxx). 

A pre-print of the original paper titled ***"Program Feature-based Benchmarking for FuzzTesting"*** can be found inside this artifact package. 

## Data

The `FeatureBench` directory contains 153 benchmark programs generated from this work. The programs are organized by feature parameters as discussed in the paper, with 13 sub-directories (groups):
  - **COMW**: Number of conditional branches (Width) - 16 programs
  - **COMD**: Number of conditional branches (Depth) - 8 programs
  - **COMWE**: Execution probability of conditional branches (Weight) - 7 programs
  - **COMB**: Execution probability of conditional branches (BBranch) - 32 programs
  - **LOOPI**: Loops and recursions (Iteration, Has_Data_Constraint=Off) - 10 programs
  - **LOOPDI**: Loops and recursions with data constraints (Iteration, Has_Data_Constraint=On) - 10 programs
  - **RECURI**: Recursions (Iteration, Has_Data_Constraint=Off) - 10 programs
  - **RECURDI**: Recursions with data constraints (Iteration, Has_Data_Constraint=On) - 10 programs
  - **MAGICS**: Magic bytes (Start) - 10 programs
  - **MAGICL**: Magic bytes (Length) - 10 programs
  - **MAGICD**: Nested magic bytes and checksum tests (Depth) - 10 programs
  - **CHECKSUMC**: Checksum tests (Count) - 10 programs
  - **CHECKSUMD**: Nested checksum tests (Depth) - 10 programs

Each benchmark program directory contains the **source code** (C files) and a **Makefile** for compilation.

The `data` directory contains the experimental data, and visualizations (heatmaps) that support the conclusions made in the two research questions (RQ1 and RQ2).
Inside the `data` directory, there are two sub-directories (`results` and `heatmaps`):

### Results
The `results` directory contains 12 CSV files with experimental results for 11 fuzzers: AFL, AFLFast, AFL++, Honggfuzz, EcoFuzz, MOpt, Fairfuzz, TortoiseFuzz, Memlock, RedQueen, and Laf-intel. 
Each CSV file corresponds to a group of benchmark programs. The results for `CHECKSUMC` and `CHECKSUMD` are saved in a single CSV file.
  
These results are used to generate the correlation results and visualizations for Research Question 2 (RQ2).

### Heatmaps
The `heatmaps` directory contains 13 heatmaps, each displaying the **Mann-Whitney U test (p-value)** for program pairwise runtime comparisons in the `COMB` benchmark group for each fuzzer. Note that TortoiseFuzz and Memlock have two variants, so each has two heatmaps.

## Setup

The `code` directory contains the source code of the benchmark generation scripts used in Section 4 and the experiment scripts used in Section 5. 
Inside the `code` directory, there are two sub-directories (`generator` and `experiments`):

### Requirements