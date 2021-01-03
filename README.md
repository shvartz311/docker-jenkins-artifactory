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


The above commands were used to run the 3 containers I used for this project: Artifactor OSS, Docker dind and Jenkins container with blueocean.

These are the following tasks I had to accomplish:

1. Create Dockerfile as follows:

a.      Based on Ubuntu latest image

b.      Define environment variable VERSION=1.2.0

c.      Install python

d.      Install vim

e.      Install zip

f.      Install unzip

g.      Copy zip_job.py into the images /tmp folder

h.      Once docker container is up run a command which will print OS type and
architecture + verify /tmp/zip_job.py exists
 
2.       Create zip_job.py python script as follows:

a.       Create an array of a,b,c,d

b.       Based on this array create txt files (a.txt,b.txt….)

c.       Make sure all txt files created and if not - fail the script

d.       Create zip files with names based on array + VERSION environment

variable, that each one will have one txt file inside (a_1.2.0.zip should include
a.txt, b_1.2.0.zip should include b.txt and so on)

e.       Make sure all zip files created and if not - fail the script


3.      Create 2 Jenkinsfiles pipeline jobs with the same logic, one Declarative and
one Scripted:

a. Agent should be based on the Dockerfile you created in step 1
        i.            it should run in a privileged mode with label zip-job-docker

b.       Build stage should execute the zip_job.py youve created in step 2

c.       Publish stage should upload all the zip files created (only in case build
stage succeeded) to Artifactory using the following properties

      i.            Artifactory server ;https://artifactory-telaviv;

    ii.            Artifactory user ;super-user;

    iii.            Artifactory password ;Qw12856!;

    iv.            Artifactory repository to upload to ;binary-storage/{VERSION env
variable};

d.       Report stage - send email with job status in the subject to some email
address

e.       Cleanup stage - delete the workspace
