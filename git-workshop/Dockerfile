FROM ubuntu:latest
LABEL org.opencontainers.image.authors="scott@scottmuc.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install software-properties-common -y
RUN add-apt-repository ppa:git-core/ppa

RUN apt update && apt install -y \
  ca-certificates \
  cowsay \
  curl \
  git \
  nano \
  sudo \
  tmux \
  tmuxinator

RUN mkdir -p /etc/apt/keyrings \
  && curl -fsSL https://repo.charm.sh/apt/gpg.key | gpg --dearmor -o /etc/apt/keyrings/charm.gpg
RUN echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | tee /etc/apt/sources.list.d/charm.list
RUN apt update && apt install -y gum

# Setup the skeleton home directory so that the created user gets
# all the shell improvements
COPY skel /etc/skel/

# Entrypoint is responsible for creating linux users with the same
# UID and GID as the host system user so that the shared volume
# mount can be cleaned up easily
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]
