import sys
import socket
from datetime import datetime

def main():
    SERVER = '172.16.99.161'  # Standard loopback interface address (localhost)
    PORT = 8888        # Port to listen on (non-privileged ports are > 1023)
    openStream = str.encode('$ST')
    closeStream = str.encode('$SP')
    srvAddressPort = (SERVER, PORT)
    bufferSize = 1024

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.sendto(openStream, srvAddressPort)

    for i in range(0,10):
        msgFromSrv = UDPClientSocket.recvfrom(bufferSize)

        print(str(datetime.now().strftime("%H:%M:%S")) + ",\t" + str(msgFromSrv) + "\n")

    UDPClientSocket.sendto(closeStream, srvAddressPort)


if __name__ == '__main__':
    print('Starting...')
    main()