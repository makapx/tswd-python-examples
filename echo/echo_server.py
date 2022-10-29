"""
ECHO SERVER
Single thread echo server.
Wait for a client to connect, then echo back whatever the client sends
until the client sends the secret word
"""

import socket
import argparse

HOST = ""  # default hostname
PORT = 50007  # default port
BUFFSIZE = 1024  # buffer size
SECRET = b"mischief-managed"  # secret word to end the server


def main():
    # parsing command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("-H", "--host", type=str, default=HOST, help="Host name")
    parser.add_argument("-p", "--port", type=int, default=PORT, help="Port number")
    args = parser.parse_args()

    # create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((args.host, args.port))
        sock.listen(1)

        # loop until the client sends the secret word
        while True:
            # return a new socket object representing the connection with the client
            # decoupling tuple of (socket, address) of the client
            conn, addr = sock.accept()
            with conn:
                print("Connected by", addr)
                while True:
                    # receive data from the client
                    data = conn.recv(BUFFSIZE)

                    # connection closed
                    if not data:
                        break

                    # echo back the data
                    conn.sendall(data + b" from server")

                    # print data for server views
                    print("Received", data)
                    # if the client sends the secret word, break the loop
                    if data == SECRET:
                        return


if __name__ == "__main__":
    main()
