# 1. Image Docker sshd
- link: https://hub.docker.com/r/rastasheep/ubuntu-sshd
- Docker Pull Command: docker pull rastasheep/ubuntu-sshd
- link github: https://github.com/rastasheep/ubuntu-sshd
- root password: root
## Run example
```bash
$ sudo docker run -d -P --name test_sshd rastasheep/ubuntu-sshd:18.04
$ sudo docker port test_sshd 22
  0.0.0.0:49154

$ ssh root@localhost -p 49154
# The password is `root`
root@test_sshd $
```
# 2. Install Package
```bash
apt update
apt upgrade
```
Inside an ubuntu 20.04 container (```bashdocker run -ti ubuntu:20.04```):
```bash
apt-get update
apt-get install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
# Install py39 from deadsnakes repository
apt-get install python3.9
# Install pip from standard ubuntu packages
apt-get install python3-pip
```
Then you can run python 3.9 with ```bash python3.9 ```
# 3. Install anaconda 
- Step 1:  Download Anaconda
	Download file anaconda.sh from https://www.anaconda.com/products/distribution
- Step 2: Copy file anaconda.sh inside container 
- Step 3: Run the Script
```bash
bash Anaconda3-2020.07-Linux-x86_64.sh
```
- Step 4: Activate and Test Installation
To activate the installation, type the following command:
```bash
source ~/.bashrc
```
To test the installation, type the conda command below:
```bash
conda list
```
- Step 5: Set Up Anaconda Environments
```bash
conda create --name yolov5 python=3
```



