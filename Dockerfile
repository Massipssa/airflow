FROM ubuntu:20.04

LABEL maintainer="kerrache.massipssa@gmail.com"
LABEL version="0.0.1"
LABEL description="This is test image from travis"

ENV NAME=TOTO

RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip

COPY src/ /mydir

EXPOSE 8080

ENTRYPOINT ["/bin/bash", "-c", "echo Hello, $NAME"]
