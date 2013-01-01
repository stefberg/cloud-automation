#!/usr/bin/python

import cgi
import subprocess

form = cgi.FieldStorage()

print "Content-Type: text/plain"
print ""
if not form.has_key("pass") or form["pass"].value != "shaberg":
    print "Wrong password!"
    exit()
if not form.has_key("group"):
    print "must set a group name"
    exit()

print "Starting an instancew with size", form["vm_size"].value, "adding it to puppet group", form["group"].value
out_file = open("/var/www/logs/provision.txt", "w")
subprocess.call(["/home/ubuntu/bootstrap_node", form["group"].value], stdout=out_file)
out_file.close()
in_file = open("/var/www/logs/provision.txt", "r")
print in_file.read()
in_file.close()
