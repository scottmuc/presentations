FROM ubuntu:latest
LABEL org.opencontainers.image.authors="scott@scottmuc.com"

RUN apt-get update && apt-get install -y \
  cowsay \
  git \
  nano \
  sudo \
  tmux \
  tmuxinator

# Setup the skeleton home directory so that the created user gets
# all the shell improvements
COPY dot.bash_profile /etc/skel/.bash_profile
COPY dot.bashrc /etc/skel/.bashrc
COPY dot.gitconfig /etc/skel/.gitconfig
COPY dot.tmux.conf /etc/skel/.tmux.conf
COPY tmuxinator.handsongit.yml /etc/skel/.config/tmuxinator/handsongit.yml
COPY tmuxinator.funwithremotes.yml /etc/skel/.config/tmuxinator/funwithremotes.yml
COPY instructions.txt /etc/skel/instructions.txt

COPY commit_something /etc/skel/bin/commit_something
COPY fun_with_remotes /etc/skel/bin/fun_with_remotes
COPY banner_watcher /etc/skel/bin/banner_watcher

# Entrypoint is responsible for creating linux users with the same
# UID and GID as the host system user so that the shared volume
# mount can be cleaned up easily
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]
