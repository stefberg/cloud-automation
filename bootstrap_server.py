#!/usr/bin/python

import SocketServer
import subprocess
import os

if os.path.exists('/var/www/html/logs'):
    log_file="/var/www/html/logs/provision.txt"
else:
    log_file="/var/www/logs/provision.txt"

class BootstrapHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print self.data
        out_file = open(log_file, "w")
        params = self.data.split()
        subprocess.call(["./bootstrap_node", params[0], params[1]], stdout=out_file)
        out_file.close()
        in_file = open(log_file, "r")
        in_data = in_file.read()
        in_file.close()
        # just send back the same data, but upper-cased
        self.request.sendall(in_data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9080
    # Create the server, binding to localhost on port
    server = SocketServer.TCPServer((HOST, PORT), BootstrapHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    print "Starting server...."
    server.serve_forever()
