import socket

# Caesar Cipher Decryption Function
def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift_value = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_value - shift) % 26 + shift_value)
        else:
            decrypted += char
    return decrypted

def server_program():
    host = "127.0.0.1"  # Localhost
    port = 12345  # Port number

    server_socket = socket.socket()  # Create socket object
    server_socket.bind((host, port))  # Bind the host and port

    server_socket.listen(1)  # Allow one connection at a time
    print(f"Server is listening on {host}:{port}...")
    
    conn, address = server_socket.accept()  # Accept connection
    print(f"Connection from {address}")

    shift = 3  # Caesar cipher shift (same shift used by the client)
    
    while True:
        # Receive data from client
        data = conn.recv(1024).decode()
        if not data:
            break  # If no data, close connection

        print("Encrypted message received:", data)

        # Decrypt message using Caesar cipher
        decrypted_message = caesar_decrypt(data, shift)
        print("Decrypted message:", decrypted_message)

        # Send back the decrypted message as server response
        response = "Server response: " + decrypted_message
        conn.send(response.encode())  # Send response back to client

    conn.close()  # Close connection

if __name__ == '__main__':
    server_program()
