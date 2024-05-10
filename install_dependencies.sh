#!/bin/bash

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

export DEBIAN_FRONTEND=noninteractive

# Ensure the script is run as root
if [ "$(id -u)" -ne 0 ]; then
   echo -e "${RED}This script must be run as root${NC}" 1>&2
   exit 1
fi

# Update and Upgrade the system
echo -e "${GREEN}Updating and upgrading your system...${NC}"
apt-get update --quiet
apt-get upgrade -y --quiet

# Install kernel headers and development packages
echo -e "${GREEN}Installing kernel headers...${NC}"
apt-get install linux-headers-$(uname -r)

# Remove outdated signing keys
echo -e "${GREEN}Removing outdated signing keys...${NC}"
apt-key del 7fa2af80

# Install new cuda-keyring
DISTRO='ubuntu2204'
ARCH='x86_64'
echo -e "${GREEN}Install new cuda-keyring for ${DISTRO} on ${ARCH}...${NC}"
wget -N https://developer.download.nvidia.com/compute/cuda/repos/$DISTRO/$ARCH/cuda-keyring_1.1-1_all.deb
dpkg -i cuda-keyring_1.1-1_all.deb

# Update package list
echo -e "${GREEN}Updating package list...${NC}"
apt-get update --quiet

# Install NVIDIA driver
echo -e "${GREEN}Installing the NVIDIA driver...${NC}"
apt-get install -y --quiet nvidia-driver-550

# Install CUDA Toolkit 12.0
echo -e "${GREEN}Installing CUDA Toolkit 12.0...${NC}"
apt-get install -y --quiet cuda-12-0

# Determine the original user's home directory
USER_HOME=$(getent passwd $SUDO_USER | cut -d: -f6)
# Path to the original user's .profile
PROFILE="$USER_HOME/.profile"

# Set up the environment variables
echo -e "${GREEN}Setting up the environment variables...${NC}"
echo "export PATH=/usr/local/cuda/bin:\$PATH" >> ${USER_HOME}/.profile
echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:\$LD_LIBRARY_PATH" >> ${USER_HOME}/.profile

# Install other dependencies
apt-get install -y --quiet cmake binutils


echo -e "${GREEN}Installation completed successfully.${NC}"

# Function to handle SIGINT (Ctrl-C)
function handle_ctrl_c {
    echo -e "${RED}Reboot cancelled by user.${NC}"
    exit 1  # Exit the script without rebooting
}

# Trap SIGINT and call handle_ctrl_c function when it's caught, but only enable it just before the countdown
echo -e "${RED}System will reboot in 10 seconds. Press Ctrl-C to cancel.${NC}"
trap handle_ctrl_c SIGINT

# Countdown loop
for (( i=10; i>0; i-- )); do
    echo -n "$i..."
    sleep 1
done

# Disable the trap after the countdown is complete to prevent it from catching SIGINT later
trap - SIGINT

echo -e "${GREEN}Rebooting now...${NC}"
sleep 1
reboot
