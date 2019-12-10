# -*- coding=utf-8 -*-
import zmq

context = zmq.Context()

recive = context.socket(zmq.PULL)
recive.connect('tcp://127.0.0.1:8818')

sender = context.socket(zmq.PUSH)
sender.connect('tcp://127.0.0.1:8819')

while True:
    data = recive.recv()
    print "正在转发..."
    sender.send(data)
