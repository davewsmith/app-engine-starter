# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8080, host:8080
  config.vm.network "forwarded_port", guest: 8000, host:8000
  config.vm.network "private_network", ip: "10.10.10.10"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "App Engine VM"
    vb.memory = 1024
    vb.cpus = 1
  end

  config.vm.provision :shell, path: "provision.sh"
end
