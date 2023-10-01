# Builder Image
FROM python:3.10.3-slim-bullseye

# Install Dependencies
RUN apt-get -y update


RUN pip3 install ultralytics
RUN pip3 install paddlepaddle
RUN pip3 install "paddleocr>=2.0.1"
RUN apt-get install -y libgl1-mesa-glx libglib2.0-0