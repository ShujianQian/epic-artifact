#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

ARTIFACT_ROOTDIR=$(pwd)
echo -e "${GREEN}Starting in directory: ${ARTIFACT_ROOTDIR}${NC}"

EPIC_DIR=${ARTIFACT_ROOTDIR}/epic
echo -e "${GREEN}Building Epic in ${EPIC_DIR}${NC}"
mkdir ${EPIC_DIR}/build
cd ${EPIC_DIR}/build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j

STO_DIR=${ARTIFACT_ROOTDIR}/sto
echo -e "${GREEN}Building STO in ${STO_DIR}${NC}"
cd ${STO_DIR}
./bootstrap.sh
./configure
make -j PROFILE_COUNTERS=1 DEBUG_ABORTS=0 BOUND=7 ADAPTIVE=1 NDEBUG=0 FINE_GRAINED=1 tpcc_bench ycsb_bench

CARACAL_DIR=${ARTIFACT_ROOTDIR}/caracal
echo -e "${GREEN}Building Caracal in ${CARACAL_DIR}${NC}"
mkdir ${CARACAL_DIR}/build
cd ${CARACAL_DIR}/build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_CXX_FLAGS=-stdlib=libc++ "-DCMAKE_EXE_LINKER_FLAGS=-stdlib=libc++ -lc++abi" ..
make -j

# Cannot build Aria along side caracal because libc++ conflicts with google-glog
# see: https://github.com/rust-lang/crates-build-env/issues/125
# see also: https://bugs.launchpad.net/ubuntu/+source/google-glog/+bug/1991919

# ARIA_DIR=${ARTIFACT_ROOTDIR}/aria
# echo -e "${GREEN}Building Aria in ${ARIA_DIR}${NC}"
# cd ${ARIA_DIR}
# ./compile.sh