#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color


ARTIFACT_ROOTDIR=$(pwd)
echo -e "${GREEN}Starting in directory: ${ARTIFACT_ROOTDIR}${NC}"

mkdir -p ${ARTIFACT_ROOTDIR}/data/epic
mkdir -p ${ARTIFACT_ROOTDIR}/data/caracal/tpcc
mkdir -p ${ARTIFACT_ROOTDIR}/data/caracal/tpccfull
mkdir -p ${ARTIFACT_ROOTDIR}/data/caracal/ycsb
mkdir -p ${ARTIFACT_ROOTDIR}/data/sto

echo -e "${GREEN}Parsing Epic reulsts...${NC}"
python3 ./epic/parse_expriments.py ./epic/epic_output/ ./data/epic/

echo -e "${GREEN}Parsing Caracal reulsts...${NC}"
python3 ./caracal/parse_caracal_result.py ./caracal/caracal_ycsb_output/ ./data/caracal/ycsb/
python3 ./caracal/parse_caracal_ycsb_latency_result.py ./caracal/caracal_ycsb_output/ ./data/caracal/ycsb/
python3 ./caracal/parse_tpcc_result.py ./caracal/caracal_tpcc_output/ ./data/caracal/tpcc/
python3 ./caracal/parse_tpcc_latency_result.py ./caracal/caracal_tpcc_output/ ./data/caracal/tpcc/

echo -e "${GREEN}Parsing STO reulsts...${NC}"
python3 ./sto/parse_ycsb_results.py ./sto/sto_output/ ./data/sto
python3 ./sto/parse_tpccfull_results.py ./sto/sto_output/ ./data/sto/
python3 ./sto/parse_tpcc_results.py ./sto/sto_output/ ./data/sto/