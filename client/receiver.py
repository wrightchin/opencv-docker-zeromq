#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
# socket.connect("tcp://0.0.0.0:5001")
socket.bind("tcp://*:5001")
# socket = context.socket(zmq.SUB)
# socket.connect("tcp://pub:5001")
# socket.setsockopt_string(zmq.SUBSCRIBE,"")

print("Starting")
while True:
    #  Wait for next request from client
    # print("waiting")
    message = socket.recv().decode()
    print (message)
    # message = socket.recv_string()
    # print (message)
    # print(f"Received request: {message}")
    # faces = message.decode()
    # if (int(faces) >= 2):
    #     print("Alert! " + faces + " faces detected")
    # else:
    #     print("Safe " + faces + " face only")

    #  Do some 'work'
    # time.sleep(1)

    #  Send reply back to client
    socket.send(b"200")