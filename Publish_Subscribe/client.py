# -*- coding=utf-8 -*-
import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:8818")
socket.setsockopt(zmq.SUBSCRIBE,'')  # 消息过滤

while True:
    response = socket.recv();
    print("response: %s" % response)
