# The Artifacts for Program Feature-based Benchmarking for FuzzTesting

## Table of Contents

- [The Artifacts for Program Feature-based Benchmarking for FuzzTesting](#the-artifacts-for-program-feature-based-benchmarking-for-fuzztesting)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [Provenance](#provenance)
  - [Getting Started](#getting-started)
    - [Requirements](#requirements)
    - [Generate the Benchmark Programs](#generate-the-benchmark-programs)
    - [Fuzz the Benchmark Programs](#fuzz-the-benchmark-programs)
  - [Detailed Description](#detailed-description)
    - [Structure of the Artifact](#structure-of-the-artifact)
      - [FeatureBench](#featurebench)
      - [Data](#data)
        - [Results](#results)
        - [Heatmaps](#heatmaps)
      - [Code](#code)
        - [Generator](#generator)
        - [Experiments](#experiments)
    - [Replicating the major results](#replicating-the-major-results)


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

### Getting Started
We provide smaller experiments to verify the functionality of the artifact in this section, as replicating the major paper results is expected to take hundreds of hours of machine time.

#### Requirements

The evaluation of this artifact does not require specific hardware. However, the following software and hardware specifications are recommended:

- Linux (tested with Ubuntu 22.04.3 LTS);
- Docker (tested with version 25.0.2);
- Python (tested with version 3.10.12)

#### Generate the Benchmark Programs

First, ensure that you are in the `code/generator` directory:

`cd code/generator`

Then, run the following command to generate the benchmark programs for the `COMD` group as an example:

```commandline
python3 generate_prog_comp.py comd --out COMD_PROG
```

This will create a `COMD_PROG` folder containing 8 generated C source code files for the `COMD` benchmark group.

Next, run the following command to generate the benchmark programs for the `COMD` group:

```commandline
python3 generate_benchmark_num.py COMD_PROG --out COMD
```

This will create a `COMD` folder containing 8 generated benchmark programs for the `COMD` group.

#### Fuzz the Benchmark Programs

First, ensure that you are in the `code/experiments` directory:

`cd code/experiments`

To run the experiments using the `testfuzz`, run the following command:

```commandline
cd testfuzz && bash build.sh fast COMD 30
```
where `fast` is the power schedule, `COMD` is the benchmark group, and `30` can be configured to the timeout (unit: second) you wish to use. 
This will create a `results` folder and a `reports` in the `code/experiments` directory.

We explain the structure of the results through the `testfuzz` example above:

```commandline
reports
|- csvs
|  |- COMD
|  |  |- 20250408
|  |  |  |- metrics
|  |  |  |  |- testfuzz_fast.csv
results
|- COMD
|  |- testfuzz_fast
|  |  |- 202504081716
|  |  |  |- COMP_W2_D4_B1
|  |  |  |  |- 0
|  |  |  |  |  |- default
|  |  |  |  |  |  |- crashes
|  |  |  |  |  |  |  |- id:000000,sig:06,src:000000,time:179,execs:165,op:arith8,pos:0,val:-7
|  |  |  |  |  |  |- hangs
|  |  |  |  |  |  |  |- ...
|  |  |  |  |  |  |- lcov
|  |  |  |  |  |  |  |- coverage.json
|  |  |  |  |  |  |- profraw
|  |  |  |  |  |  |  |- id:000000,time:0,execs:0,orig:seed.profraw
|  |  |  |  |  |  |  |- id:000001,src:000000,time:3,execs:9,op:quick,pos:0,+cov.profraw
|  |  |  |  |  |  |  |- ...
|  |  |  |  |  |  |- queue
|  |  |  |  |  |  |  |- id:000000,time:0,execs:0,orig:seed
|  |  |  |  |  |  |  |- id:000001,src:000000,time:3,execs:9,op:quick,pos:0,+cov
|  |  |  |  |  |  |  |- ...
|  |  |  |  |  |  |- ...
|  |  |  |  |  |  |- fuzz_bitmap
|  |  |  |  |  |  |- fuzzer_setup
|  |  |  |  |  |  |- fuzzer_stats
|  |  |  |  |  |  |- ...
|  |  |  |  |  |- runtime_log.txt
|  |  |  |  |- ...
|  |  |  |  |- 19
|  |  |  |  |  |- ...
```

By default, the fuzzer runs each benchmark program for 20 iterations. The results of each iteration are stored in their respective folders. Within each iteration folder, the fuzzing output includes coverage data, crash reports, hang information, other relevant metrics, and a runtime log (`runtime_log.txt`). 
The profraw files (`.profraw`) are generated by llvm-cov, which is used to collect the coverage information. The `lcov` folder contains the coverage information in JSON format (`coverage.json`). 
Finally, fuzzing statistics are extracted from both the `fuzzer_stats` and `coverage.json` files to generate a csv report (`testfuzz_fast.csv`), which is stored in the `reports` folder.

## Detailed Description

### Structure of the Artifact

#### FeatureBench

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

#### Data

The `data` directory contains the experimental data, and visualizations (heatmaps) that support the conclusions made in the two research questions (RQ1 and RQ2).
Inside the `data` directory, there are two sub-directories (`results` and `heatmaps`).

##### Results
The `results` directory contains 12 CSV files with experimental results for 11 fuzzers: AFL, AFLFast, AFL++, Honggfuzz, EcoFuzz, MOpt, Fairfuzz, TortoiseFuzz, Memlock, RedQueen, and Laf-intel. 
Each CSV file corresponds to a group of benchmark programs. The results for `CHECKSUMC` and `CHECKSUMD` are saved in a single CSV file.
These results are used to generate the correlation results and visualizations for Research Question 2 (RQ2).

##### Heatmaps
The `results` directory contains 13 heatmaps, each displaying the **Mann-Whitney U test (p-value)** for program pairwise runtime comparisons in the `COMB` benchmark group for each fuzzer. Note that TortoiseFuzz and Memlock have two variants, so each has two heatmaps.

#### Code

The `code` directory contains two sub-directories (`generator` and `experiments`), which contain the source code of the benchmark generation scripts used in Section 4 and the experiment scripts used in Section 5, respectively. 

##### Generator

The `generator` directory contains 3 sub-directories: `config`, `template_char`, and `template_num`, and 11 python scripts:
  - **config**: Contains 13 configuration files for the benchmark generation scripts. Each configuration file corresponds to a group of benchmark programs.
  - **template_char**: Contains one template C file and a Makefile for generating the benchmark programs for the `LOOPI`, `LOOPDI`, `RECURI`, `RECURDI`, `MAGICS`, `MAGICL`, `MAGICD`, `CHECKSUMC`, and `CHECKSUMD` groups.
  - **template_num**: Contains three template C files or header files, and a Makefile for generating the benchmark programs for the `COMW`, `COMD`, `COMWE`, and `COMB` groups.
  - **generate_benchmark_char.py**: Generates the benchmark programs based on the configuration files and the `template_char` template.
  - **generate_benchmark_num.py**: Generates the benchmark programs based on the configuration files and the `template_num` template.
  - **generate_prog_xxx.py**: Generates the C source code for each benchmark program under the respective groups. 

  _Note: `generate_prog_comp.py` generates programs for the `COMW` and `COMD` groups, `generate_prog_magic.py` generates programs for the `MAGICS`, `MAGICL`, and `MAGICD` groups, and `generate_prog_checksum.py` generates programs for the `CHECKSUMC` and `CHECKSUMD` groups._

##### Experiments

The `generator` directory contains 14 sub-directories, 13 of which correspond to a fuzzer or its variants. In total, we evaluate 11 fuzzers, including `AFL`, `AFLFast`, `AFL++`, `Honggfuzz`, `EcoFuzz`, `MOpt`, `FairFuzz`, `TortoiseFuzz`, `Memlock`, `RedQueen`, and `Laf-Intel`. 

_Note: Memlock has two variants: Heap and Stack. TorotiseFuzz has two variants: bb and loop._

The additional sub-directory, `testfuzz`, is provided for testing purpose for the _Getting Started_ evaluation, which reuses the `AFL++` docker image. There a small benchmark, `testbench`, inside the `testfuzz` directory, which contains 1 benchmark program `COMP_W2_D4_B1` and a `seed` directory with 1 seed input file.

Inside each fuzzer directory, there is a `coverage` sub-directory, a `build.sh` script, a `Dockerfile`, and a `report.py` script:
  - **coverage**: Contains a `coverage.sh` script that collects the coverage information.
  - **build.sh**: Compiles the benchmark programs, build the docker image, runs the fuzzer inside the docker container, and generates the final report.
  - **Dockerfile**: Contains the instructions to build the docker image for each fuzzer.
  - **report.py**: Extracts the coverage information from the fuzzer output and generates final reports.

_Note: For ecofuzz, there is an additional script `static_module.sh` to aid in its fuzzing process._

### Replicate the major results

#### Generate the Complete Benchmark Programs

Navigate to the `code/generator` directory:

```commandline
cd code/generator
```
and run the following 24 commands to generate the benchmark programs for all groups.
Alternatively, you can execute the shell script `generate_all.sh`.

```commandline

# Generate benchmark programs for COMD group
python3 generate_prog_comp.py comd --out COMD_PROG
python3 generate_benchmark_num.py COMD_PROG --out COMD

# Generate benchmark programs for COMW group
python3 generate_prog_comp.py comw --out COMW_PROG
python3 generate_benchmark_num.py COMW_PROG --out COMW

# Generate benchmark programs for COMB group
python3 generate_prog_comb.py --out COMB_PROG
python3 generate_benchmark_num.py COMB_PROG --out COMB

# Generate benchmark programs for COMWE group
python3 generate_prog_comwe.py --out COMWE_PROG
python3 generate_benchmark_num.py COMWE_PROG --out COMWE

# Generate benchmark programs for LOOPI group
python3 generate_prog_loop.py --out LOOPI_PROG
python3 generate_benchmark_char.py LOOPI_PROG --out LOOPI

# Generate benchmark programs for LOOPDI group
python3 generate_prog_loop_data.py --out LOOPDI_PROG
python3 generate_benchmark_char.py LOOPDI_PROG --out LOOPDI

# Generate benchmark programs for RECURI group
python3 generate_prog_recur.py --out RECURI_PROG
python3 generate_benchmark_char.py RECURI_PROG --out RECURI

# Generate benchmark programs for RECURDI group
python3 generate_prog_recur_data.py --out RECURDI_PROG
python3 generate_benchmark_char.py RECURDI_PROG --out RECURDI

# Generate benchmark programs for MAGICS group
python3 generate_prog_magic.py magics --out MAGICS_PROG
python3 generate_benchmark_char.py MAGICS_PROG --out MAGICS

# Generate benchmark programs for MAGICL group
python3 generate_prog_magic.py magicl --out MAGICL_PROG
python3 generate_benchmark_char.py MAGICL_PROG --out MAGICL

# Generate benchmark programs for MAGICD group
python3 generate_prog_magic.py magicd --out MAGICD_PROG
python3 generate_benchmark_char.py MAGICD_PROG --out MAGICD

# Generate benchmark programs for CHECKSUMC group
python3 generate_prog_checksum.py checksumc --out CHECKSUMC_PROG
python3 generate_benchmark_char.py CHECKSUMC_PROG --out CHECKSUMC

# Generate benchmark programs for CHECKSUMD group
python3 generate_prog_checksum.py checksumd --out CHECKSUMD_PROG
python3 generate_benchmark_char.py CHECKSUMD_PROG --out CHECKSUMD_PROG

```
#### Evaluate All Fuzzers on FeatureBench

Evaluate all fuzzers on FeatureBench is expected to require hundreds of hours of machine time and significant system memory. Please ensure that sufficient computing resources are available before running these commands. For reference, the experiments in our paper were conducted on a server with an AMD Ryzen Threadripper PRO 5975WX CPU (64 threads) and 128GB RAM.

To evaluate all fuzzers on all program groups in FeatureBench, navigate to the `code/experiments` directory: 

```commandline
cd code/experiments
```
and run the following 13 commands to evaluate all fuzzers on all groups in FeatureBench.
Alternatively, you can execute the shell script `fuzz_all.sh`.

```commandline

# Evaluate all fuzzers on COMD group. 
bash fuzz_all_COMW.sh

# Evaluate all fuzzers on COMW group.
bash fuzz_all_COMW.sh

# Evaluate all fuzzers on COMB group.
bash fuzz_all_COMB.sh

# Evaluate all fuzzers on COMWE group.
bash fuzz_all_COMWE.sh

# Evaluate all fuzzers on LOOPI group.
bash fuzz_all_LOOPI.sh

# Evaluate all fuzzers on LOOPDI group.
bash fuzz_all_LOOPDI.sh

# Evaluate all fuzzers on RECURI group.
bash fuzz_all_RECURI.sh

# Evaluate all fuzzers on RECURDI group.
bash fuzz_all_RECURDI.sh

# Evaluate all fuzzers on MAGICS group.
bash fuzz_all_MAGICS.sh

# Evaluate all fuzzers on MAGICL group.
bash fuzz_all_MAGICL.sh

# Evaluate all fuzzers on MAGICD group.
bash fuzz_all_MAGICD.sh

# Evaluate all fuzzers on CHECKSUMC group.
bash fuzz_all_CHECKSUMC.sh

# Evaluate all fuzzers on CHECKSUMD group.
bash fuzz_all_CHECKSUMD.sh

```
After all the experiments are completed, the results will be saved in the `results` and `reports` directories as 
described in the _Fuzz the Benchmark Programs_ section.