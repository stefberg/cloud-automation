
# Install python additions
sudo apt-get install python-pip
sudo apt-get install python-dev
sudo pip install -U boto
sudo pip install -U paramikop

# Download puppet-enterprise-2.7.0-ubuntu-12.04-amd64.tar.gz 
# to this directory and uncompress it
gunzip puppet-enterprise-2.7.0-ubuntu-12.04-amd64.tar.gz 

# Create a key pair to be used by the provsioner in the puppet master
# Do not set a password for the key.
ssh-keygen -t rsa -f puppet_provisioner

# Upload the public key to AWS with the same name

#Create .fog file in the home directory
#:default:
#  :aws_access_key_id: " aws_key
#  :aws_secret_access_key: " aws_secret

# and the same info in ~/.boto
#[Credentials]
#aws_access_key_id = aldjflakdfj
#aws_secret_access_key = lkadsflkjafd

touch .ssh/known_hosts
