# -*- coding=utf-8 -*-

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:8818")

socket.send('Are you OK?')
response = socket.recv();
print("response: %s" % response)
