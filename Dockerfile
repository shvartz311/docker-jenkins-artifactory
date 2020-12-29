FROM ubuntu:latest
#ENV VERSION="1.2.0" deprecated this as stating it in the dockerfile and bringing it into the python script is kind of a waste when you can use -e at docker run command
RUN apt-get update && apt-get install -y \
  python3 \
  vim \
  zip \
  unzip
COPY ./zip_job.py /tmp/
CMD ["sh","-c","cat /etc/os-release && [ -f /tmp/zip_job.py ]"]

