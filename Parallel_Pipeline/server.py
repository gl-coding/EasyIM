# -*- coding=utf-8 -*-
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:8818")

while True:
    socket.send("测试消息")
    print "已发送"    
    time.sleep(1) 
