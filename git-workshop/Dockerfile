FROM ubuntu:latest

ENV TERM=xterm-256color

RUN apt-get update && apt-get install -y \
  cowsay \
  git \
  tmux \
  tmuxinator

COPY dot.gitconfig /root/.gitconfig
COPY dot.tmux.conf /root/.tmux.conf
COPY tmuxinator.yml /root/.config/tmuxinator/workshop.yml
COPY entrypoint.sh /entrypoint.sh


