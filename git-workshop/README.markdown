# Hands on Git

## Abstract

A hands on way to interact and learn git with **as few** abstractions as possible.

## How To Begin

**Windows** - Recommended to launch this in a shared Windows mount in WSL (e.g.: /mnt/c/Users/...)
This will allow for viewing the repository in Windows native applications like VS Code, etc.

**Mac** - Needs to be launched from a path that can be mounted in the docker engine (e.g.: ~/foo)

**Linux** - No special path specific instructions

Copy + paste the following into your terminal

```bash
docker pull ghcr.io/scottmuc/handsongit:latest
docker run -it --rm \
  -v $PWD:/workspace \
  -w /workspace \
  -e UID="$(id -u)" \
  -e GID="$(id -g)" \
  -e USER="handsongit" \
  -e HOME="/home/handsongit" \
  ghcr.io/scottmuc/handsongit:latest
```

Once you see a prompt that resembles something like:

`handsongit@036eb4b7ad3e:/workspace$ `

Now you can run either:

- `start_graph_workshop`
- `start_gitremotes_workshop`

To quit, enter the command relevant to the workshop you're running:

- `stop_graph_workshop`
- `stop_gitremotes_workshop`

The workshop is designed to follow [this script](../git/README.markdown).
