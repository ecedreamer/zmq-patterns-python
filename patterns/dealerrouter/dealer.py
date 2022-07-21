# encoding: utf-8

import random
import zmq
import time

context = zmq.Context()
worker = context.socket(zmq.DEALER)
worker.setsockopt_string(zmq.IDENTITY, str(random.randint(0, 8000)))
worker.connect("tcp://localhost:5559")
start = False
worker.send_string("Hello")
while True:
    if start:
        worker.send_string(f"recording data: {random.randint(0, 100)}")
        time.sleep(0.5)
    request = worker.recv_string()
    if request == "START":
        start = True
    elif request == "STOP":
        start = False
    if request == "END":
        print("A is finishing")
        break