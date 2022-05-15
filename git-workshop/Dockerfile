FROM ubuntu:latest

ENV TERM=xterm-256color

RUN apt-get update && apt-get install -y \
  cowsay \
  git \
  sudo \
  tmux \
  tmuxinator

COPY dot.bashrc /tmp/.bashrc
COPY dot.gitconfig /tmp/.gitconfig
COPY dot.tmux.conf /tmp/.tmux.conf
COPY tmuxinator.yml /tmp/.config/tmuxinator/workshop.yml
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]
