# build docker file
```bash
docker build -t yolo:v8 -f Dockerfile_arm64 .
```

# run folder docker 
```bash
docker run -itd --name "docker_container_name" --mount source=ai-checkin,destination=/home/ yolo:v8
```
- example: 
```bash
docker run -itd --name yolov8_ctn --mount type=bind,source="$(pwd)",destination=/home yolo:v8

docker run -itd --name yolov8_ctn --mount type=bind,source=$PWD,destination=/home yolo:v8
```

# exec docker container 
```bash
docker exec -it "docker_container_name" bash
```
- example:
```bash
docker exec -it yolov8_ctn bash
```