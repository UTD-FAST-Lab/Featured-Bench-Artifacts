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