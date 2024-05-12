#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Ensure the script is run as root
if [ "$(id -u)" -ne 0 ]; then
   echo -e "${RED}This script must be run as root${NC}" 1>&2
   exit 1
fi

echo -e "${GREEN}Setting up huge pages...${NC}"
sysctl -w vm.nr_hugepages=50000