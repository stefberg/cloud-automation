#!/bin/sh

file=/etc/puppetlabs/puppet/auth.conf
host=`hostname -f`
cert_status="path /certificate_status\nmethod save\nauth any\nallow `hostname -f`\n"

if [ ! -f $file.orig ]
then
  cp $file $file.orig
fi
sed "s|# this one is not stricly necessary|$cert_status\n# this one is not stricly necessary|" < $file.orig > $file
diff $file.orig $file 

file=/opt/puppet/lib/site_ruby/1.8/puppet/cloudpack.rb
if [ ! -f $file.orig ]
then
  cp $file $file.orig
fi

sed 's/# TODO: Wait for C.S.R.?/sleep(10)/' <$file.orig > $file
diff $file.orig $file 



