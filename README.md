# epic-artifact

This site provides the artifacts needed to run the experiments described in the paper "Massively Parallel Multi-Versioned Transaction Processing" accepted at OSDI 2024.

Please follows the three steps shown below: 1) Setup (virtual machine) server, 2) Prepare server for the experiments, and 3) Run experiments on server.

## 1. Setup (virtual machine) server

1. Use your brower to access FluidStack at https://console.fluidstack.io and then login in with the provided credentials. Click on the "Virtual Machines" tab to create a virtual machine.

![FluidStack Homepage](<figs/1-welcome.png>)

2. Select `Ubuntu 22.04 (Plain)` for the OS template.

![OS Template](<figs/2-os-template.png>)

3. Select `RTX A6000 48GB` for the GPU server type. Select `4` GPUs per server.

![GPU Type](<figs/3-gpu-selection.png>)

4. Add your SSH public key to access the server. If you have a github public key, you can copy and paste it from https://github.com/[gitusername].keys. Also, name your server so that you can identify it.

![SSH Keys](<figs/4-ssh-key.png>)

5. Now you are ready to deploy your server. Check the server configuration and then push the deploy button.

![Deploy server](<figs/5-deploy.png>)

6. Click on the "Your Servers" tab to see your server. Wait for your server to start running. You will see a green dot on the left when your server is running. This might take a minute or so.

![All Servers](<figs/6-all-servers.png>)

7. Click on your server. To login to the server via `ssh`, you will need to use the username `ubuntu` and the IP address shown on the right.

![Server](<figs/7-server.png>)

8. When the server is not in use, stop the server to only pay the idle rate. You can restart the server at any time and continue using it.

![Manage Server](<figs/8-manage-server.png>)

9. <mark>Make sure to delete the server after finishing the experiments to stop paying for the server. If you need to rerun the experiments, then you will need to redo all the steps shown here.</mark>

## 2. Prepare server for the experiments
1. Login to the the server.
   ```bash
   ssh ubuntu@server_ipaddr
   ```
1. Clone this repo with submodules.
   ```bash
   git clone --recursive https://github.com/ShujianQian/epic-artifact.git
   ```
1. Install dependencies.
   ```bash
   cd epic-artifact
   sudo ./install_dependencies.sh
   ```
   This script installs all the dependencies required for the experiments, including the GPU driver. The script requires sudo privileges to install packages on your server. It will run for roughly 10 minutes, so get a coffee.

   <mark> At the end, the script will reboot the server to start running the GPU driver.</mark>
1. Reconnect to the server after it has rebooted and go to the artifact directory.
   ```bash
   ssh ubuntu@server_ipaddr
   cd epic-artifact
   ```
1. Build the executables for all systems using the build_binaries.sh script.
   ```bash
   ./build_binaries.sh
   ```
   This script will run for roughly 4 minutes.
## 3. Running Experiments
1. Run the following script to run the experiments.
   ```bash
   # in epic-artifact
   ./run_experiments.sh
   ```
   This script will run the experiments for roughly 4.5 hours.

## 4. Process the Experiment Output
1. Run the following script to parse the output of the experiments.
   ```bash
   # in epic-artifact
   ./parse_experiments.sh
   ```
   The parsed outputs will be stored under the `epic-artifact/data/` directory.
2. Run the following script to generate the figures shown in the paper using the parsed outputs.
   ```bash
   # in epic-artifact
   ./plot.sh
   ```
   This script will create the following figures under `epic-artifact/output/`.
   ```
   04_tpccfull_throughput.png  05a_tpccnp_throughput.png  05b_tpccnp_throughput_gacco_commutative.png  06_ycsb_throughput.png  07_cpu_throughput.png  09_latency.png  10_microbenchmark.png
   ```
   The file names for each figure has a number label (e.g., `04`) that is the same as the figure number (e.g., `Figure 4`) in the paper.


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
