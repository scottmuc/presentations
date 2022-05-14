#!/bin/bash
# https://github.com/tsari/docker-entrypoint

set -e

function createUser() {
    useradd --system --gid=$GID --uid=$UID $USER
}

function createGroup() {
    groupadd --system --gid=$GID $USER
}

function renameUser() {
    usermod -l $USER -d /home/$USER $1
}

function getUserById() {
    echo $(getent passwd "$UID" | awk -F: '{print $1}')
}

function getGroupById() {
    echo $(getent group "$GID" | awk -F: '{print $1}')
}

# Execute as user set in dockerfile, when no other user was passed in docker run command.
if [ -z "$GID" ] || [ -z "$USER" ]; then
    exec "$@"
else
    # check if group already exist and use this group or create a new one
    existingGroup=$(getGroupById)
    if [ -z "$existingGroup" ]; then
        createGroup
        existingGroup=$(getGroupById)
    fi

    # check if user already exists and use this user or create a new one
    existingUser=$(getUserById)
    if [ -z "$existingUser" ]; then
        createUser
        existingUser=$(getUserById)
    fi

    if [ $existingUser != $USER ]; then
        renameUser $existingUser
    fi

    # execute as non-root user
    exec sudo -E -u "$USER" "$@"
fi
