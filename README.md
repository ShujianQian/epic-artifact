# epic-artifact

This site provides the artifacts needed to run the experiments described in the paper "Massively Parallel Multi-Versioned Transaction Processing" accepted at OSDI 2024.

Please follows the three steps shown below: 1) Setup (virtual machine) server, 2) Prepare server for the experiments, and 3) Run experiments on server.

## 1. Setup (virtual machine) server
1. Use your brower to access FluidStack at https://console.fluidstack.io and then login in with the provided credentials. Click on the Virtual Machines tab to create a virtual machine.
![FluidStack Homepage](<figs/1-welcome.png>)
1. Select Ubuntu 22.04 (Plain) for the OS template.
![OS Template](<figs/2-os-template.png>)
1. Select RTX A6000 48GB for the GPU server type. Select 4 GPUs per server.
![GPU Type](<figs/3-gpu-selection.png>)
1. Add your SSH public key to access the server. If you have a github public key, you can copy and paste it from https://github.com/&lt;gitusername&gt;.keys. Also, name your server so that you can identify it.
![SSH Keys](<figs/4-ssh-key.png>)
1. Now you are ready to deploy your server. Check the server configuartion and then push the deploy button.
![Deploy server](<figs/5-deploy.png>)
1. Click on the Your Servers tab to see your server. Wait for your server to start running. You will see a green dot on the left when your server is running.
![All Servers](<figs/6-all-servers.png>)
1. Click on your server. To login to the server, you will need to use the username "ubuntu" and the IP address shown on the top right.
![Server](<figs/7-server.png>)
1. When the server is not in use, stop the server to only pay the idle rate. You can restart the server at any time and continue using it. Restarting a server takes a minute or so.
![Manage Server](<figs/8-manage-server.png>)
1. <mark>Make sure to delete the server after finishing the experiments to stop paying for the server. If you need to redo the experiments, then you will need to redo all the steps shown here.</mark>

## 2. Prepare server for the experiments
1. ssh to the server
1. clone this repo with submodules using
   ```bash
   git clone --recursive https://github.com/ShujianQian/epic-artifact.git
   ```
1. install dependencies with
   ```bash
   cd epic-artifact
   sudo ./install_dependencies.sh
   ```
   This script installs all dependencies required for the experiment including the GPU driver. At the end of the script, it will reboot the server to start running the GPU driver. Reconnect SSH after rebooting.

   <mark>The script requires sudo privilege to install the packages.</mark>
1. build the executables for all systems using the build_binaries.sh script.
   ```bash
   cd epic-artifact
   ./build_binaries.sh
   ``` 
   <mark>Make sure the pwd is in the repo root before running the script.</mark>

## 3. Running Experiments
WIP


## Problems
1. Aria's dependencies cannot be installed alongside those for Caracal
    - This is because the libunwind required by Aria's google-glog package conflits with libc++ and libc++abi required by Caracal.
    - see: https://github.com/rust-lang/crates-build-env/issues/125
    - see also: https://bugs.launchpad.net/ubuntu/+source/google-glog/+bug/1991919
    - As a result, Aria experiments are not run as part of this repo.

## Notes
1. Run `nvidia-smi` to verify that the Nvidia driver is running
   ```bash
   ubuntu@recwt9dgzwtn8yqxuax3htpzv:~$ nvidia-smi
    Sat May 11 08:40:22 2024
    +-----------------------------------------------------------------------------------------+
    | NVIDIA-SMI 550.54.15              Driver Version: 550.54.15      CUDA Version: 12.4     |
    |-----------------------------------------+------------------------+----------------------+
    | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
    |                                         |                        |               MIG M. |
    |=========================================+========================+======================|
    |   0  NVIDIA RTX A4000               Off |   00000000:00:05.0 Off |                  Off |
    | 41%   37C    P8              6W /  140W |       1MiB /  16376MiB |      0%      Default |
    |                                         |                        |                  N/A |
    +-----------------------------------------+------------------------+----------------------+

    +-----------------------------------------------------------------------------------------+
    | Processes:                                                                              |
    |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
    |        ID   ID                                                               Usage      |
    |=========================================================================================|
    |  No running processes found                                                             |
    +-----------------------------------------------------------------------------------------+
   ```
