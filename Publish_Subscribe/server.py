# -*- coding=utf-8 -*-
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:8818")

while True:
    print('发送消息')
    socket.send("消息群发")
    time.sleep(1)    
