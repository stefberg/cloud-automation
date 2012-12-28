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

ec2 = boto.ec2.connect_to_region('eu-west-1')

print "Starting..."
started = ec2.run_instances('ami-c1aaabb5',
                  key_name='vbox-ubuntu',
                  instance_type='t1.micro',
                  security_groups=['quick-start-1'])

instance = started.instances[0]
print "started ", instance.id, " ", instance._state.name, " ", instance.public_dns_name

print "waiting for instance to start",
while instance.state != 'running':
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(1)
    instance.update()
print ""

print "started ", instance.id, " ", instance._state.name, " ", instance.public_dns_name

wait_time = 60
print "wait", wait_time, "before connecting with ssh..."
time.sleep(wait_time)
print 'connecting with ssh...'
ssh_client = boto.manage.cmdshell.sshclient_from_instance(instance, '/home/saberg/.ssh/id_rsa',
                                                          host_key_file='~/.ssh/known_hosts',
                                                          user_name='ubuntu', ssh_pwd=ssh_pass)

print ssh_client.run('arch')

ec2.close()
print "done\n"
