# build docker file
```bash
docker build -t alpr:v1 -f Dockerfile .
```
# exec docker container 
```bash
docker exec -it "docker_container_name" bash
```
- example: 
```bash
docker exec -it alpr_ctn bash
```

# run folder docker 
```bash
docker run -itd --name "docker_container_name" -p 5000:5000 --mount source=ai-checkin,destination=/home/ alpr:v1
```
- example: 
```bash
docker run -itd --name alpr_ctn -p 5000:5000 --mount type=bind,source="$(pwd)",destination=/home alpr:v1

docker run -itd --name alpr_ctn -p 5000:5000 --mount type=bind,source=$PWD,destination=/home alpr:v1
```

# restart docker container
```bash
docker restart "my_container"
```
- example: 
```bash
docker restart alpr_ctn
```

# stop container 
```bash
docker stop my_container
```
- ex: 
```bash
docker stop alpr_ctn
```

# show log container 
```bash
sudo docker logs -f alpr_ctn
```