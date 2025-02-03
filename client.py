import socket

def client_program():
    host = "127.0.0.1"  # Server address
    port = 12345  # Port number

    client_socket = socket.socket()  # Create socket object
    client_socket.connect((host, port))  # Connect to server

    while True:
        message = input("Enter message to send to server: ")  # Get user input

        client_socket.send(message.encode())  # Send message to server
        data = client_socket.recv(1024).decode()  # Receive response from server

        print("Server:", data)

        if message.lower() == "exit":
            break  # Exit the loop if 'exit' message is sent

    client_socket.close()  # Close the connection

if __name__ == '__main__':
    client_program()
