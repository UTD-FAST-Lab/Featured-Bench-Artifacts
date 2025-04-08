# Featured-Bench-Artifacts# Artifact for Program Feature-based Benchmarking for FuzzTesting

This repository contains the FeatureBench, experimental data, and visualizations (heatmaps) for the paper titled **"Program Feature-based Benchmarking for FuzzTesting"**.

## Repository Structure

- **FeatureBench Directory**: This directory contains 153 benchmark programs generated from this work. The programs are organized by feature parameters as discussed in the paper, with 13 sub-directories (groups):
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

## Data Directory
The `data` directory contains 12 CSV files with experimental results for 11 fuzzers: AFL, AFLFast, AFL++, Honggfuzz, EcoFuzz, MOpt, Fairfuzz, TortoiseFuzz, Memlock, RedQueen, and Laf-intel. 
Each CSV file corresponds to a group of benchmark programs. The results for `CHECKSUMC` and `CHECKSUMD` are saved in a single CSV file.
  
These results are used to generate the correlation results and visualizations for Research Question 2 (RQ2).

## Heatmaps Directory
The `heatmaps` directory contains 13 heatmaps, each displaying the **Mann-Whitney U test (p-value)** for program pairwise runtime comparisons in the `COMB` benchmark group for each fuzzer. Note that TortoiseFuzz and Memlock have two variants, so each has two heatmaps.
