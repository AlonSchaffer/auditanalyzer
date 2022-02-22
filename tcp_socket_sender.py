import os
import socket
import logging
import json
from signal import signal, SIGPIPE, SIG_DFL

def send_json_to_port(objects):
    #signal(SIGPIPE,SIG_DFL)
    HOST = 'localhost'
    PORT = 1234
    SEND_TO_PORT = 514
    json_objects = json.dumps(objects)
    #create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket opend')
    try:
        sock.bind((HOST, PORT))
        print('socket connected')
        sock.sendto(json_objects.encode(), ('localhost', SEND_TO_PORT))
    except BrokenPipeError:
        sock.close()
