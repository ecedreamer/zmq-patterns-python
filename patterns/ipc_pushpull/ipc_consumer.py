import time
import zmq
import random

def consumer():
    consumer_id = random.randrange(1,10005)
    print(f"I am consumer #{consumer_id}")
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("ipc://ipc_pushpull")
   
    while True:
        work = consumer_receiver.recv_json()
        data = work['num']
        result = { 'consumer' : consumer_id, 'num' : data}
        print(result)

if __name__ == '__main__':
    consumer()