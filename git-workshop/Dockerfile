FROM ubuntu:latest
LABEL org.opencontainers.image.authors="scott@scottmuc.com"

RUN apt-get update && apt-get install software-properties-common -y
RUN add-apt-repository ppa:git-core/ppa
RUN apt-get update && apt-get install -y \
  cowsay \
  curl \
  git \
  gum \
  nano \
  sudo \
  tmux \
  tmuxinator

# Setup the skeleton home directory so that the created user gets
# all the shell improvements
COPY skel /etc/skel/

# Entrypoint is responsible for creating linux users with the same
# UID and GID as the host system user so that the shared volume
# mount can be cleaned up easily
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]