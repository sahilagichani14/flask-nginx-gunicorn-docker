#!/bin/bash

eval "$(ssh-agent -s)"
if [ ! -d "/root/.ssh/" ]; then
    ssh-add -k /root/.ssh/id_rsa
    # ssh-add -k /run/secrets/id_rsa
    mkdir /root/.ssh
    chmod 400 /root/.ssh/
    ssh-keyscan git.cs.uni-paderborn.de > /root/.ssh/known_hosts
    # now execute command which require authentication via ssh (example, git clone from a private repo)
fi

# Get the hostname
HOSTNAME=$(hostname)
# Generate SSH key with hostname as the comment
yes | ssh-keygen -t rsa -C "$HOSTNAME" -f "$HOME/.ssh/id_rsa" -P ""
# Check if SSH key generation was successful
if [ $? -eq 0 ]; then
    echo "SSH key generated successfully."
    # Display the public key
    cat ~/.ssh/id_rsa.pub
else
    echo "Failed to generate SSH key."
fi