# build docker file
# into alpr_project
```
docker build -t yolo:v8 -f code/yolov8/Dockerfile_arm64 .
```

# run folder docker 
```
docker run -itd --name "docker_container_name" --mount source=ai-checkin,destination=/home/ yolo:v8
```
- example: 
```
docker run -itd --name yolov8_ctn --mount type=bind,source="$(pwd)",destination=/home yolo:v8


docker run -itd --name yolov8_ctn --mount type=bind,source=$PWD,destination=/home yolo:v8
```

# exec docker container 
```
docker exec -it "docker_container_name" bash
```
- example:
```
docker exec -it yolov8_ctn bash
```

# train 
yolo train model=yolov8n.pt data=alpr.yaml epochs=1 imgsz=640 batch=8

# predict
yolo predict model=alpr_yolov8n_8000img_43epoch.pt source=../../test_video/test_1.mp4 save_txt

