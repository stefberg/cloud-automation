#!/bin/sh

release='ubuntu'
[ -f /etc/redhat-release ] && release='redhat'

file=/etc/puppetlabs/puppet/auth.conf
host=`hostname -f`
#cert_status="path /certificate_status\nmethod save\nauth any\nallow `hostname -f`\n"

if [ ! -f $file.orig ]
then
  cp $file $file.orig
fi

sed ":a;N;\$!ba;s/auth yes\nallow pe-internal-dashboard/auth any\nallow pe-internal-dashboard,$host/g" < $file.orig > $file
#sed "s|# this one is not stricly necessary|$cert_status\n# this one is not stricly necessary|" < $file.orig > $file
diff $file.orig $file 

file=/opt/puppet/lib/site_ruby/1.8/puppet/cloudpack.rb
[ release = 'redhat' ] && file=/opt/puppet/lib/ruby/site_ruby/1.8/puppet/cloudpack.rb
if [ ! -f $file.orig ]
then
  cp $file $file.orig
fi

sed 's/# TODO: Wait for C.S.R.?/sleep(10)/' <$file.orig > $file
diff $file.orig $file 

auth_user=stefberg1@gmail.com
auth_password=secret_password
cd /opt/puppet/share/console-auth
/opt/puppet/bin/rake db:create_user USERNAME="${auth_user}" PASSWORD="${auth_password}" ROLE="Admin"

cd 

if [ $release = 'ubuntu' ]
then
    cp provision.html /var/www/
    cp provision.py /usr/lib/cgi-bin
    chmod +x /usr/lib/cgi-bin/provision.py
    mkdir /var/www/logs
    chmod go+w /var/www/logs
fi
if [ $release = 'redhat' ]
then
    cp provision.html /var/www/html
    cp provision.py /var/www/cgi-bin
    chmod +x /var/www/provision.py
    mkdir /var/www/html/logs
    chmod go+w /var/www/html/logs
fi

chmod +x bootstrap_server.py

file=.puppet/modules/puppetlabs-dashboard/lib/puppet/dashboard/classifier.rb 
if [ ! -f $file.orig ]
then
  cp $file $file.orig
fi

sed 's/\\w/[\\w\\.]/g' <$file.orig > $file

chmod +x create_ya_classes
./create_ya_classes