# docker-sample

% cat Dockerfile 
FROM amazonlinux:latest
CMD echo "Hello"
ENTRYPOINT ["tail", "-f", "/dev/null"]

docker build -t hello .

docker run -d hello

