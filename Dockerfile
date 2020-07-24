FROM ubuntu:20.04

LABEL maintainer="kerrache.massipssa@gmail.com"
LABEL version="0.0.1"
LABEL description="This is test image from travis"

# define variables that will be avaibale only inside image (while buildin image)
ARG MAIN="main.py"

# define default variables. Can be accessed from the outside
ENV NAME=TOTO

RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip

COPY src/ /mydir

WORKDIR /mydir

RUN ls /mydir
RUN python $MAIN

# create group and user
ENV GROUP_GID=1010
ENV USER_UID=1010

RUN addgroup --gid "${GROUP_GID}" "testgroup" && \
    adduser --quiet "testuser" --uid "${USER_UID}" \
        --ingroup "testgroup" \
        --home "/home/testuser"

EXPOSE 8080

ENTRYPOINT ["/bin/bash", "-c", "echo Hello, $NAME"]
