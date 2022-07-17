# 1. Image Docker 
- document of yolov5: https://docs.ultralytics.com/environments/Docker-Quickstart/
- download docker image at docker hub
```bash
sudo docker pull ultralytics/yolov5:latest
```
## Run example
```bash
 docker run --shm-size 8G --ipc=host -it -v "%cd%"/data_docker:/usr/src/data_docker ultralytics/yolov5:latest
```
# 2. Install Package
```bash
apt update
apt upgrade
```
- copy data to folder data_docker
- start docker container 
- window: cd into folder contain data_docker
 ```bash
 docker run --shm-size 8G --ipc=host -it -v "%cd%"/data_docker:/usr/src/data_docker ultralytics/yolov5:latest
```
- macOS: cd into folder contain train_yolov5
 ```bash
sudo docker run --shm-size 8G --ipc=host -it -v "$(pwd)"/train_yolov5:/usr/src/train_yolov5 ultralytics/yolov5:latest
 ```
- RuntimeError: a view of a leaf Variable that requires grad is being used in an in-place operation.
 ```bash
pip install torch==1.7.0+cu110 torchvision==0.8.1+cu110 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
 ```
- Pytesseract : "TesseractNotFound Error: tesseract is not installed or it's not in your path", how do I fix this?
On Linux
```bash
sudo apt-get update
sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
 ```