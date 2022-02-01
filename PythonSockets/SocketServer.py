import sys
import socket
from datetime import datetime

def main():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 7700        # Port to listen on (non-privileged ports are > 1023)
    txtFile = open('newsocklog_' + str(datetime.now().strftime("%H%M%S")) + ".txt", "w+")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                txtFile.write(str(datetime.now().strftime("%H:%M:%S")) + ",\t" + str(data) + "\n")
                print(str(datetime.now().strftime("%H:%M:%S")) + ",\t" + str(data) + "\n")
                if not data:
                    break
                conn.sendall(data)

if __name__ == '__main__':
    print('Starting...')
    main()