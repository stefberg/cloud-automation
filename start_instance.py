#!/usr/bin/python
# in ~/.boto
# add this
#[Credentials]
#aws_access_key_id = aldjflakdfj
#aws_secret_access_key = lkadsflkjafd

import boto
import boto.ec2.connection

ec2 = boto.ec2.connect_to_region('eu-west-1')
print "Starting...\n"

ec2.run_instances('ami-c1aaabb5',
                  key_name='vbox-ubuntu',
                  instance_type='t1.micro',
                  security_groups=['quick-start-1'])
print "started\n"
ec2.close()
print "done\n"
