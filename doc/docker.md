#1. Image Docker sshd
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