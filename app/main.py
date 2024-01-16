import socket


def main():
    print("Logs from your program will appear here!")

    # Bind the socket to a specific address and port
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    # new socket object that the server can use to communicate with the connected client, tuple with address
    client_socket, address = server_socket.accept()

    # receive data from the client with 1024 bytes (max)
    request_data = client_socket.recv(1024).decode("utf-8")

    # request_data =
    # GET /index.html HTTP/1.1
    # Host: localhost:4221
    # User-Agent: curl/7.64.1
    data_elements_list = request_data.split("\r\n")[0]
    request_method, request_path, request_http_version = data_elements_list.split(" ")
    response_body = request_path.split("/")[2:]
    response_body_str = "/".join(response_body)

    if request_path == "/":
        # send response
        response = "HTTP/1.1 200 OK\r\n\r\n"
    elif request_path.startswith("/echo"):
        # GET /echo/abc HTTP/1.1
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body_str)}\r\n\r\n{response_body_str}"
    else:
        response = "HTTP/1.1 404 Not Found \r\n\r\n"

    client_socket.sendall(response.encode())

    # Closing socket
    client_socket.close()


if __name__ == "__main__":
    main()
