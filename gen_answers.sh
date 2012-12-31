#!/bin/sh
if [ "$2" = "" ]
then
    echo Usage: $0 '<console login emaail> <console password>'
    exit 1
fi

echo q_install=y
echo q_puppet_cloud_install=y
echo q_puppet_enterpriseconsole_auth_database_name=console_auth
echo q_puppet_enterpriseconsole_auth_database_password=4aEPCffzxlTEC0DpGf1Q
echo q_puppet_enterpriseconsole_auth_database_user=console_auth
echo q_puppet_enterpriseconsole_auth_password=$2
echo q_puppet_enterpriseconsole_auth_user_email=$1
echo q_puppet_enterpriseconsole_database_install=y
echo q_puppet_enterpriseconsole_database_name=console
echo q_puppet_enterpriseconsole_database_password=NBN6SVcxqYJPd6ju1hyz
echo q_puppet_enterpriseconsole_database_remote=n
echo q_puppet_enterpriseconsole_database_root_password=IBwgCNNJFgCjPgyaOTZP
echo q_puppet_enterpriseconsole_database_user=console
echo q_puppet_enterpriseconsole_httpd_port=443
echo q_puppet_enterpriseconsole_install=y
echo q_puppet_enterpriseconsole_inventory_hostname=`hostname -f`
echo q_puppet_enterpriseconsole_inventory_port=8140
echo q_puppet_enterpriseconsole_master_hostname=`hostname -f`
echo q_puppet_enterpriseconsole_smtp_host=localhost
echo q_puppet_enterpriseconsole_smtp_password=
echo q_puppet_enterpriseconsole_smtp_port=25
echo q_puppet_enterpriseconsole_smtp_use_tls=n
echo q_puppet_enterpriseconsole_smtp_user_auth=n
echo q_puppet_enterpriseconsole_smtp_username=
echo q_puppet_symlinks_install=y
echo q_puppetagent_certname=`hostname -f`
echo q_puppetagent_install=y
echo q_puppetagent_server=`hostname -f`
echo q_puppetca_install=y
echo q_puppetmaster_certname=`hostname -f`
echo q_puppetmaster_dnsaltnames=`hostname`,`hostname -f`,puppet,puppet.eu-west-1.compute.internala
echo q_puppetmaster_enterpriseconsole_hostname=localhost
echo q_puppetmaster_enterpriseconsole_port=443
echo q_puppetmaster_install=y
echo q_vendor_packages_install=y
