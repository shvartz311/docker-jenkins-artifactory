"# docker-jenkins-artifactory" 
docker run -it --rm -v ${PWD}:/work -w /work --entrypoint /bin/sh centos

yum install -y jq gzip nano tar git unzip wget

Build with:

docker build -t example -f Dockerfile .
To run the container:

docker run -e VERSION=1.2.0 --rm --name example example

docker run --name artifactory -d --network jenkins -p 8081:8081 -p 8082:8082 docker.bintray.io/jfrog/artifactory-oss:latest

#docker 1

docker run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind


#docker 2

docker run --name jenkins-blueocean --rm --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --publish 8080:8080 --publish 50000:50000 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro myjenkins-blueocean:1.1