# python-flask-docker
Basic Python Flask app in Docker which prints the hostname and IP of the container

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/lvthillo/python-flask-docker.git
$ docker build -t lvthillo/python-flask-docker .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/lvthillo/python-flask-docker/).
```
docker pull lvthillo/python-flask-docker
```

### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 8080:8080 lvthillo/python-flask-docker
```

Now visit http://localhost:8080
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' my-container
6095273a4e9b
```

## Concentrated commands
docker build -t connorli0/connor-test:1.4 .
docker push connorli0/connor-test:latest
- ```docker build -t connorli0/connor-test:1.4 .``` for building the image with tag 1.4
- ```docker push connorli0/connor-test:latest``` for pushing the image to docker hub
- ```docker run -d -p 8080:8080 connorli0/connor-test:latest``` for running the image on port 8080
- ```docker ps``` for checking the running containers
- ```docker stop <container id>``` for stopping the container
- ```docker rm <container id>``` for removing the container
- ```docker rmi <image id>``` for removing the image
- ```docker images``` for checking the images
- ```docker pull <image name>``` for pulling the image from docker hub
- ```docker exec -it <container id> /bin/bash``` for entering the container
- ```docker logs <container id>``` for checking the logs of the container
- ```docker inspect <container id>``` for checking the container details


