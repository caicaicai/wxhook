#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import httplib, urllib
import socket
import time
import os.path
import json
import re
import datetime
from time import gmtime, strftime
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080


def send_msg(MESSAGE):
    TCP_IP = '10.255.255.18'
    TCP_PORT = 8001
    BUFFER_SIZE = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    # print "received data:", data

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
        #Handler for the GET requests
        def do_POST(self):
                # path_params = self.path.split("/")
                content_len = int(self.headers.getheader('content-length', 0))
                post_body = self.rfile.read(content_len)
                msg = json.loads(post_body, encoding="UTF-8")
                # send_msg(msg['content'])
                # print(msg['content'])
                # print(type(msg['content']))
                # print(type("你"))
                content = msg['content']

                send_msg( content.encode('utf8'))

                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send the html message
                self.wfile.write("{}")
                return


if __name__ == '__main__':
    try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print 'Started httpserver on port ' , PORT_NUMBER

        #Wait forever for incoming htto requests
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()