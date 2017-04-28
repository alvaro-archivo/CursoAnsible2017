# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|

  config.vm.define 'vagrant1' do |v|
    v.vm.box = 'ubuntu/xenial64'
    v.vm.boot_timeout = 400
    v.vm.network 'private_network', ip: '192.168.33.20'
    v.vm.synced_folder '.', '/vagrant', disable: true
    v.vm.network :forwarded_port, guest: 22, host: 2222, id: "ssh"
    v.vm.provider 'virtualbox' do |vb|
      vb.name = 'Vagrant-Curso Ansible 1'
    end
  end

  config.vm.define 'vagrant2' do |v|
    v.vm.box = 'ubuntu/xenial64'
    v.vm.network 'private_network', ip: '192.168.33.21'
    v.vm.synced_folder '.', '/vagrant', disable: true
    v.vm.network :forwarded_port, guest: 22, host: 2200, id: "ssh"
    v.vm.provider 'virtualbox' do |vb|
      vb.name = 'Vagrant-Curso Ansible 2'
    end
  end

end
