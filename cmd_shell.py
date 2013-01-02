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
#puppet_console_email = raw_input('puppet console email: ')
#puppet_console_pass = getpass.getpass('puppet console password: ')
#aws_key = raw_input('aws_access_key_id: ')
#aws_secret = raw_input('aws_secret_access_key: ')

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

print "starting bootstrap server"
run_cmd('./bootstrap_server.py > bootstrap.log &')
exit()

print "running gen_answers.sh"
run_cmd('sh ./gen_answers.sh ' + puppet_console_email + " " + puppet_console_pass + " > answers.txt")
print "running puppet installation"
run_cmd('cd puppet-enterprise-2.6.0-ubuntu-12.04-amd64; sudo ./puppet-enterprise-installer -a ../answers.txt')
print "running pe_post_patch.sh"
run_cmd('sudo pe_post_patch.sh')
print "creating .fog file"
f = open("fog", "w")
f.write(":default:\n  :aws_access_key_id: " + aws_key + "\n  :aws_secret_access_key: " + aws_secret + "\n")
f.close()

ssh_client.put_file("fog", ".fog")

print "now add user stefberg1@gmail.com with password secret_password on the PE console"
