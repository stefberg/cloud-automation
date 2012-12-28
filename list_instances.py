#!/usr/bin/python
# in ~/.boto
# add this
#[Credentials]
#aws_access_key_id = aldjflakdfj
#aws_secret_access_key = lkadsflkjafd

import boto
import boto.ec2.connection

ec2 = boto.ec2.connect_to_region('eu-west-1')

print "instances:\n"
instances = ec2.get_all_instances()
for i in instances:
    for k in i.instances:
        print k.id, k._state.name, k.public_dns_name

ec2.close()
print "done\n"
