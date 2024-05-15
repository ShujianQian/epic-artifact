#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color


ARTIFACT_ROOTDIR=$(pwd)
echo -e "${GREEN}Starting in directory: ${ARTIFACT_ROOTDIR}${NC}"

EPIC_DIR=${ARTIFACT_ROOTDIR}/epic
echo -e "${GREEN}Running Epic experiments in ${EPIC_DIR}${NC}"
cd ${EPIC_DIR}
python3 ./test_experiments.py

echo -e "${GREEN}Starting Caracal controller...${NC}"

cleanup_caracal_controller() {
    echo "Cleaning up caracal controller..."
    kill $CONTROLLER_PID
}

trap cleanup_caracal_controller EXIT SIGINT SIGTERM

java -jar ${ARTIFACT_ROOTDIR}/caracal-controller.jar ${ARTIFACT_ROOTDIR}/caracal-controller-config.json &
CONTROLLER_PID=$!
sleep 5 # wait for the controller to finish initialization

CARACAL_DIR=${ARTIFACT_ROOTDIR}/caracal
echo -e "${GREEN}Running Caracal in ${CARACAL_DIR}${NC}"
cd $CARACAL_DIR
bash ./test_tpcc.sh ${CARACAL_DIR}/caracal_tpccfull_output ${CARACAL_DIR}/build/dbfull
bash ./test_tpcc.sh ${CARACAL_DIR}/caracal_tpcc_output ${CARACAL_DIR}/build/db
bash ./test_ycsb.sh ${CARACAL_DIR}/caracal_ycsb_output ${CARACAL_DIR}/build/db

STO_DIR=${ARTIFACT_ROOTDIR}/sto
echo -e "${GREEN}Running STO experiments in ${STO_DIR}${NC}"
cd $STO_DIR
bash ./test_my_tpcc.sh ${STO_DIR}/sto_output
bash ./test_my_tpccfull.sh ${STO_DIR}/sto_output
bash ./test_my_ycsb.sh ${STO_DIR}/sto_output

echo -e "${GREEN}Experiment runs finished, try to notify the user...${NC}"
cd ${ARTIFACT_ROOTDIR}
bash ./mail.sh