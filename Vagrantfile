# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  config.ssh.forward_agent = true

  config.vm.define :vagrant_augur do |vagrant_host|
    vagrant_host.vm.box = "generic/ubuntu1604"
    vagrant_host.vm.define "augur"
    vagrant_host.vm.hostname = "augur" 
    vagrant_host.vm.provider "virtualbox" do |v|
      v.name = "augur"
    end

    vagrant_host.vm.network "forwarded_port", guest: 3333, host: 3333
    vagrant_host.vm.network "forwarded_port", guest: 5000, host: 5000

    if Vagrant::Util::Platform.windows? then
      config.vm.synced_folder ".", "/vagrant/augur", type: "rsync", rsync__auto: true, rsync__exclude: ['./frontend/node_modules']
    else
      if vagrant_host.vm.provider "virtualbox" then
        config.vm.synced_folder ".", "/vagrant/augur", type: 'virtualbox', SharedFoldersEnableSymlinksCreate: false
      else
        vagrant_host.vm.synced_folder ".", "/vagrant/augur", type: "rsync", rsync__auto: true, rsync__exclude: ['./frontend/node_modules*']
      end
    end
    # documentation for more information about their specific syntax and use.
    vagrant_host.vm.provision "shell", path: "util/packaging/vagrant/provision.sh"
    vagrant_host.vm.provision "shell", inline: "cd /vagrant/augur && $AUGUR_PIP install --upgrade .", privileged: true
  end

end
