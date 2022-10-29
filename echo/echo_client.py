"""
ECHO CLIENT
Send a message to the server and receive the same message back
End both client and server by sending the secret word
"""

import socket
import argparse

HOST = "localhost"  # The remote host
PORT = 50007  # The same port as used by the server
BUFFSIZE = 1024  # Buffer size
SECRET = "mischief-managed"  # secret word to end the server


def main():

    # parsing command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", type=str, default=HOST, help="Host name")
    parser.add_argument("-p", "--port", type=int, default=PORT, help="Port number")
    args = parser.parse_args()

    # create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((args.host, args.port))

        # loop until the user enters the secret word
        while True:
            message = input("Enter message: ")
            sock.sendall(message.encode())
            data = sock.recv(BUFFSIZE)
            print("Received", repr(data))

            if message == SECRET:
                break


if __name__ == "__main__":
    main()
