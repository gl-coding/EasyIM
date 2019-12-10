# -*- coding=utf-8 -*-

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:8819")

while True:
    response = socket.recv();
    print("response: %s" % response)
