#!/usr/bin/python

import sys
import getpass
import boto.manage.cmdshell

if len(sys.argv) < 3:
    print "usage: ", sys.argv[0], "<id> <dns_name>"
    exit(1)

instance_id = sys.argv[1]
dns_name = sys.argv[2]

class FakeInstance(object):

    def __init__(self, instance_id, dns_name):
        self.dns_name = dns_name
        self.id = instance_id


ssh_pass = getpass.getpass('ssh key password: ')

instance = FakeInstance(instance_id, dns_name)

ssh_client = boto.manage.cmdshell.sshclient_from_instance(instance, '/home/saberg/.ssh/id_rsa',
                                                          host_key_file='~/.ssh/known_hosts',
                                                          user_name='ubuntu', ssh_pwd=ssh_pass)

def run_cmd(cmd):
    result = ssh_client.run(cmd)
    if result[1]:
        print result[1]
    if result[2]:
        print "ERROR:", result[2]

run_cmd('ls -la')

res = ssh_client.put_file('bootstrap_node', 'bootstrap_node')
if res:
    print res

run_cmd('ls -la')



