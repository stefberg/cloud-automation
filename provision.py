#!/usr/bin/python

import cgi
import socket
import sys

form = cgi.FieldStorage()

print "Content-Type: text/html"
print ""
if not form.has_key("pass") or form["pass"].value != "shaberg":
    print "Wrong password!"
    exit()
if not form.has_key("group"):
    print "must set a group name"
    exit()

print "<html>"
print "<body>"
print "Starting an instance with size", form["vm_size"].value, "adding it to puppet group", form["group"].value, "<br/>"
print '<a href="/logs/provision.txt">log here</a>', '<br/>'
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

print "bootstrap command", data, "sent to the bootstratp server", "<br/>"
