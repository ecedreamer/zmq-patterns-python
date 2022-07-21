
# encoding: utf-8

import zmq
from collections import defaultdict

context = zmq.Context()
client = context.socket(zmq.ROUTER)
client.bind("tcp://*:5559")

poll = zmq.Poller()
poll.register(client, zmq.POLLIN)
counter = defaultdict(int)

while True:
    # handle input
    sockets = dict(poll.poll(1000))
    if sockets:
        identity = client.recv_string()
        msg = client.recv_string()
        counter[identity] += 1
    # start recording
    for identity in counter.keys():
        client.send_string(identity, zmq.SNDMORE)
        client.send_string("START")

    print(counter)