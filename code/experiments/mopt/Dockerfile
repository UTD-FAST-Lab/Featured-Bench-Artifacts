FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3-dev build-essential git wget cmake clang llvm

RUN git clone https://github.com/puppet-meteor/MOpt-AFL &&\
    cd MOpt-AFL/MOpt &&\
    make && make install

ENV CC=afl-gcc \
    CXX=afl-g++