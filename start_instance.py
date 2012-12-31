#!/usr/bin/python
# in ~/.boto
# add this
#[Credentials]
#aws_access_key_id = aldjflakdfj
#aws_secret_access_key = lkadsflkjafd

import boto
import boto.ec2.connection
import boto.manage.cmdshell
import time
import sys
import getpass

ssh_pass = getpass.getpass('ssh key password: ')
puppet_console_email = raw_input('puppet console email: ')
puppet_console_pass = getpass.getpass('puppet console password: ')
aws_key = raw_input('aws_access_key_id: ')
aws_secret = raw_input('aws_secret_access_key: ')

ec2 = boto.ec2.connect_to_region('eu-west-1')

print "Starting..."
started = ec2.run_instances('ami-c1aaabb5',
                  key_name='vbox-ubuntu',
                  instance_type='m1.small',
                  security_groups=['quick-start-1'])

instance = started.instances[0]
print instance._state.name, " ", instance.id

print "waiting for instance to start",
while instance.state != 'running':
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(1)
    instance.update()
print ""

print instance._state.name, " ", instance.id, " ", instance.public_dns_name

wait_time = 60
print "wait", wait_time, "before connecting with ssh..."
time.sleep(wait_time)
print 'connecting with ssh...'
ssh_client = boto.manage.cmdshell.sshclient_from_instance(instance, '/home/saberg/.ssh/id_rsa',
                                                          host_key_file='~/.ssh/known_hosts',
                                                          user_name='ubuntu', ssh_pwd=ssh_pass)

print ssh_client.run('arch')

class FakeInstance(object):

    def __init__(self, instance_id, dns_name):
        self.dns_name = dns_name
        self.id = instance_id



fake_instance = FakeInstance(instance.id, instance.public_dns_name)

ssh_client = boto.manage.cmdshell.sshclient_from_instance(fake_instance, '/home/saberg/.ssh/id_rsa',
                                                          host_key_file='~/.ssh/known_hosts',
                                                          user_name='ubuntu', ssh_pwd=ssh_pass)

def run_cmd(cmd):
    result = ssh_client.run(cmd)
    if result[1]:
        print result[1]
    if result[2]:
        print "ERROR:", result[2]

run_cmd('ls -la')

files = ['bootstrap_node', 'puppet-enterprise-2.6.0-ubuntu-12.04-amd64.tar', 'gen_answers.sh', 'pe_post_patch.sh']
for f in files:
    print "uploading ", f
    res = ssh_client.put_file(f, f)
    if res:
        print res

print "uploading id_rsa"
res = ssh_client.put_file("id_rsa", ".ssh/id_rsa")
if res:
    print res

print "untar puppet-enterprise-2.6.0-ubuntu-12.04-amd64.tar"
run_cmd('tar xf puppet-enterprise-2.6.0-ubuntu-12.04-amd64.tar')
print "running gen_answers.sh"
run_cmd('sh ./gen_answers.sh ' + puppet_console_email + " " + puppet_console_pass + ' > answers.txt')
print "running puppet installation"
run_cmd('cd puppet-enterprise-2.6.0-ubuntu-12.04-amd64; sudo ./puppet-enterprise-installer -a ../answers.txt')
print "running pe_post_patch.sh"
run_cmd('sudo sh ./pe_post_patch.sh')
print "creating .fog file"
f = open("fog", "w")
f.write(":default:\n  :aws_access_key_id: " + aws_key + "\n  :aws_secret_access_key: " + aws_secret + "\n")
f.close()
ssh_client.put_file("fog", ".fog")
print "install apache"
run_cmd('sudo apt-get install apache2')

run_cmd('ls -la')

ec2.close()
print "PE console https://"+instance.public_dns_name
