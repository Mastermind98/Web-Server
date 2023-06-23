import sys
from socket import * 

if __name__ == '__main__':
    # Check if the command-line arguments are provided correctly
    if len(sys.argv) != 4:
        print("The following is an input command format to run the client.\nwebclient.py <server_host> <server_port> <filename>")
        sys.exit(1)

    # Extract the command-line arguments
    SERVER_HOST = sys.argv[1]
    SERVER_PORT = int(sys.argv[2])
    FILENAME = sys.argv[3]

    # Send the HTTP request to the server and display the response
    # Create a socket instance
    client_socket = socket(AF_INET, SOCK_STREAM)

    # Prepare a client socket
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Construct the HTTP GET request
    request = f"GET /{FILENAME} HTTP/1.1\r\n"
    request += f"Host: {SERVER_HOST}\r\n"
    request += "Connection: close\r\n\r\n"

    # Send the HTTP request to the server
    client_socket.sendall(request.encode())

    # Receive and display the server response
    while True:
        response = client_socket.recv(1024).decode()
        if not response:
            break
        print(response)
client_socket.close()  
sys.exit()