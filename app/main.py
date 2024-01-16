import socket


def main():
    print("Logs from your program will appear here!")

    # Bind the socket to a specific address and port
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    # new socket object that the server can use to communicate with the connected client, tuple with address
    client_socket, address = server_socket.accept()

    # receive data from the client with 1024 bytes (max)
    request_data = client_socket.recv(1024)

    # send response ok
    response = "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.sendall(response.encode())

    # Closing socket
    client_socket.close()


if __name__ == "__main__":
    main()
