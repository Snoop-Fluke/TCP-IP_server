#!/usr/bin/env python3

import socket

HOST = '192.168.20.47'  # The server's hostname or IP address
PORT = 8090        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, GAMMM99')
    data = s.recv(1024)

print('Received', repr(data))
s.close()
