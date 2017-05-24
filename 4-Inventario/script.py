#!/usr/bin/python

import sys;

if sys.argv[1] == '--list':
	print '''
	{
		"app": {
		    "hosts": ["app1", "app2", "app3"],
		    "vars": {
		        "a": true
		    }
		},
		"db": ["db1", "db2"],
	}
	'''.strip()
else:
	print '''
	{
		"ansible_host": "127.0.0.1 ",
		"ansible_port": "2222",
		"ansible_user": "ubuntu",
		"ansible_ssh_private_key_file": "../.vagrant/machines/vagrant1/virtualbox/private_key"
	}
	'''.strip()
