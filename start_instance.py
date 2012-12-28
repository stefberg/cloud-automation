#!/usr/bin/python
# in ~/.boto
# add this
#[Credentials]
#aws_access_key_id = aldjflakdfj
#aws_secret_access_key = lkadsflkjafd

import boto
import boto.ec2.connection
import time
import sys

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

ec2.close()
print "done\n"
