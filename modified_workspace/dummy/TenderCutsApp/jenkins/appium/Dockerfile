FROM butomo1989/docker-android-x86-7.1.1

USER root
RUN apt-get update && apt-get install -y python3-pip libmysqlclient-dev

ADD requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt