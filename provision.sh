#!/bin/bash

# Provision an ubuntu/trusty64 VM for Google App Engine (Python)
#
# c.f. https://cloud.google.com/sdk/docs/#deb


# Install some quality of life stuff
sudo apt-get install -y git unzip
sudo apt-get install -y python-pip

# install Google Cloud and App Engine Python SDKs
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y google-cloud-sdk google-cloud-sdk-app-engine-python

# Testing is good
sudo pip install webtest

# Comment this in if you're paranoid. Depending on how far out of date the VM is, it might run for a while.
# sudo apt-get upgrade -y
