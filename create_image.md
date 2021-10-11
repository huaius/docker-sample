###Dockerfile
% cat Dockerfile 
# our base image
FROM amazonlinux:latest

RUN yum -y update && \
    yum -y install java && \
    yum clean all

# copy files required for the app to run
RUN mkdir -p /usr/home
WORKDIR /usr/home
COPY android ./android
COPY ios ./ios

###Create and test the image
docker build -t my_image .
docker run -it --name my my_image
docker rm my 
docker run -it --name my my_image bash

###Push Image to Docker Hub
docker login
docker tag my_image:latest huaius/bia:latest
docker push huaius/bia:latest

###Test the Image from Docker Hub
docker pull huaius/bia:latest
docker run -it huaius/bia:latest
