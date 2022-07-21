import zmq
import random
import time


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")
c = 0
while True:
    c += 1
    if c % 2 == 0:
        topic = "even"
    else:
        topic = "odd"
    print("%s %d" % (topic, c))
    socket.send_string("%s %d" % (topic, c))
    time.sleep(1)