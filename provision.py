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

print "Starting an instance with size", form["vm_size"].value, "adding it to puppet group", form["group"].value
out_file = open("/var/www/logs/provision.txt", "w")
subprocess.call(["/home/ubuntu/bootstrap_node", form["group"].value], stdout=out_file)
out_file.close()
in_file = open("/var/www/logs/provision.txt", "r")
print in_file.read()
in_file.close()

import socket
import sys

HOST, PORT = "localhost", 9080
data = form["group"].value + " " + form["vm_size"].value

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)
