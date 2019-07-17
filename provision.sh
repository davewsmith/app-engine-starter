#!/bin/bash

# Provision a VM for Google App Engine (Python)
#
# See https://cloud.google.com/sdk/docs/#deb

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python-pip

# Install some quality of life stuff
sudo apt-get install -y git zip unzip

# Install Google Cloud and App Engine Python SDKs

apt-get install apt-transport-https ca-certificates

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-python-extras google-cloud-sdk-datastore-emulator

# Testing is good
sudo pip install webtest

# TODO add the optional libraries (numpy, pandas, etc.)
