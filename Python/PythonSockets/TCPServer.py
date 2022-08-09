from concurrent.futures import thread
from copyreg import constructor
from ctypes.wintypes import tagRECT
from http import client, server
from logging import exception
import sys
import os
import socket
from threading import Thread
import random

HOST = '127.0.0.1'

def tcp_server(PORT):
    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Bind the socket to the port
            s.bind((HOST, PORT))
            print("Waiting for connection...")
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected to ', addr)
                # Receive the data in small chunks and retransmit it
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print("Received: " + str(data))
                    resp = create_response(str(data))
                    if(resp != ""):
                        conn.sendall(bytes(resp, 'utf-8'))
                        print("Sent: " + resp)

    except Exception as exc:
        print("Error caught: " + str(exc))

def create_response(rec_data):
    response = ""
    if("EMZY" in rec_data):
        response = "\x02 EMZY 0\x03"
    elif("ASTF" in rec_data):
        response = "\x02 ASTF 0\x03"
    elif("SREM" in rec_data):
        response = "\x02 SREM 0\x03"
    elif("ASTZ" in rec_data):
        response = "\x02 ASTZ 0\x03"    
    elif("SASB" in rec_data):
        response = "\x02 SASB 0\x03"
    elif("SMES" in rec_data):
        response = "\x02 SMES 0\x03"
    elif("AFSN" in rec_data):
        response = "\x02 AFSN 0 2 %s %s %s\x03" % get_random_measurements()
    elif("SEX1" in rec_data):
        response = "\x02 SEX1 0\x03"
    elif("SEX2" in rec_data):
        response = "\x02 SEX2 0\x03"
    else:
        reponse = ""

    return response

def get_random_measurements():
    return str(random.randrange(2,10)), str(random.randrange(2,10)), str(random.randrange(2,10))

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        tcp_server(sys.argv[2])
    else:
        tcp_server(23)