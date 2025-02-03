import socket

def server_program():
    # Get the host and port
    host = "127.0.0.1"  # Localhost
    port = 12345  # Port number

    server_socket = socket.socket()  # Create socket object
    server_socket.bind((host, port))  # Bind the host and port

    server_socket.listen(1)  # Allow one connection at a time
    print(f"Server is listening on {host}:{port}...")
    
    conn, address = server_socket.accept()  # Accept connection
    print(f"Connection from {address}")

    while True:
        # Receive data from client
        data = conn.recv(1024).decode()
        if not data:
            break  # If no data, close connection

        print("Received message:", data)
        response = "Server response: " + data
        conn.send(response.encode())  # Send response back to client

    conn.close()  # Close connection

if __name__ == '__main__':
    server_program()

