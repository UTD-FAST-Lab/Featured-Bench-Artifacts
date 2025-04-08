FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3-dev build-essential git wget cmake clang llvm-dev

RUN git clone https://github.com/MoonLight-SteinsGate/EcoFuzz e &&\
    mv /e/EcoFuzz / &&\
    cd /EcoFuzz && make && make install
    # cd llvm_mode && make

COPY static_module.sh /EcoFuzz/static_module.sh
RUN chmod +x /EcoFuzz/static_module.sh

ENV CC=/EcoFuzz/afl-gcc CXX=/EcoFuzz/afl-g++