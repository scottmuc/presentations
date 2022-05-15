FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
  cowsay \
  git \
  sudo \
  tmux \
  tmuxinator

# Setup the skeleton home directory so that the created user gets
# all the shell improvements
COPY dot.bash_profile /etc/skel/.bash_profile
COPY dot.bashrc /etc/skel/.bashrc
COPY dot.gitconfig /etc/skel/.gitconfig
COPY dot.tmux.conf /etc/skel/.tmux.conf
COPY tmuxinator.yml /etc/skel/.config/tmuxinator/handsongit.yml

# Entrypoint is responsible for creating linux users with the same
# UID and GID as the host system user so that the shared volume
# mount can be cleaned up easily
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]
