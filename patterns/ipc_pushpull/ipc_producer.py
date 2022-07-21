import time
import zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("ipc://ipc_pushpull")

    for num in range(15):
        work_message = { 'num' : num }
        zmq_socket.send_json(work_message)
        time.sleep(1)


if __name__ == '__main__':
    producer()
