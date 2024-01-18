import socket
import threading
import argparse
import os


def handle_request(client_socket, directory):

    # receive data from the client with 1024 bytes (max)
    request_data = client_socket.recv(1024).decode("utf-8")

    # request_data =
    # GET /index.html HTTP/1.1
    # Host: localhost:4221
    # User-Agent: curl/7.64.1
    line, header_user_agent, body = request_data.split("\r\n")[0], request_data.split("\r\n")[2], request_data.split("\r\n\r\n")[1]

    request_method, request_path, request_http_version = line.split(" ")
    response_body = request_path.split("/")[2:]

    if request_path == "/":
        # send response
        response = "HTTP/1.1 200 OK\r\n\r\n"
    elif request_path.startswith("/echo"):
        response_body_str = "/".join(response_body)
        # GET /echo/abc HTTP/1.1
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body_str)}\r\n\r\n{response_body_str}"
    elif request_path.startswith("/user-agent"):
        user_agent = header_user_agent.split(": ")[1]
        # GET /user-agent HTTP/1.1
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}"
    elif request_method == "GET" and request_path.startswith("/files"):
        file_path = os.path.join(directory, response_body[-1])
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                file_content = file.read()
            response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(file_content)}\r\n\r\n{file_content.decode()}"
        else:
            response = "HTTP/1.1 404 Not Found \r\n\r\n"
    elif request_method == "POST" and request_path.startswith("/files"):
        file_path = os.path.join(directory, response_body[-1])
        file_content = body.strip()
        with open(file_path, "wb") as file:
            file.write(file_content.encode())
        response = "HTTP/1.1 201 Created\r\n\r\n"
    else:
        response = "HTTP/1.1 404 Not Found \r\n\r\n"

    client_socket.sendall(response.encode())
    client_socket.close()


def main():
    parser_object = argparse.ArgumentParser()
    # specifying arguments that the program can accept
    parser_object.add_argument("--directory", type=str, default=".")
    # parse the arguments
    args = parser_object.parse_args()

    # Bind the socket to a specific address and port
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        # new socket object that the server can use to communicate with the connected client, tuple with address
        client_socket, address = server_socket.accept()
        # for each client new thread
        client_thread = threading.Thread(target=handle_request, args=(client_socket, args.directory))
        # make that threads run in the background
        client_thread.daemon = True
        # This starts the newly created thread, allowing the server to handle multiple client connections
        client_thread.start()


if __name__ == "__main__":
    main()
