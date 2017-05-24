#!/usr/bin/python

import sys

if sys.argv[1] == '--list':
    print '''
    {
        "aplicaciones": ["app1", "app2", "app3"],
        "bd": ["bd1", "bd2"]
    }
    '''.strip()
else:
    print '''
    {
        "ansible_host": "127.0.0.1",
        "ansible_port":"2200",
        "ansible_user": "ubuntu",
        "ansible_ssh_private_key_file: "../.vagrant/machines/vagrant2/virtualbox/private_key"
    }
    '''.strip()
