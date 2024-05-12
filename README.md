# epic-artifact

## 1. Request Virtual Machine
1. Log into FluidStack with the provided credentials and go to the virtual machines page.
<img src="figs/screenshot1.svg" alt="FluidStack Homepage">
1. Configure the virtual machine as shown in the figure. Make sure that the configuration matches exactly.
![Virtual Machine Setup](<figs/Screenshot 2024-05-11 at 4.07.36 AM.png>)
1. Push the deploy button at the bottom of the page.
1. Go to the Your Servers page, and choose the server you just created.
![alt text](<figs/Screenshot 2024-05-11 at 4.12.04 AM.png>)
1. Wait until the server request is finished and the server starts to run before connecting to the server over SSH.
![alt text](<figs/Screenshot 2024-05-11 at 4.14.40 AM.png>)
1. When not in use, stop the server to only pay idle rate
![alt text](<figs/Screenshot 2024-05-11 at 4.16.40 AM.png>)
1. <mark>Make sure to delete the server after finishing the expriment to stop paying for it.</mark>

## 2. Preparing Experiments on a Server
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
