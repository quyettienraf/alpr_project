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