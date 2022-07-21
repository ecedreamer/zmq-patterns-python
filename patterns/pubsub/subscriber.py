import sys
import zmq


# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect('tcp://localhost:5556')

topicfilter = "odd"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
while True:
    string = socket.recv_string()
    topic, messagedata = string.split()
    print(topic, messagedata)
