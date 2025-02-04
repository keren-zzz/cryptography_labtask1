import socket

# Caesar Cipher Encryption Function
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_value = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_value + shift) % 26 + shift_value)
        else:
            encrypted += char
    return encrypted

def client_program():
    host = "127.0.0.1"  # Server address
    port = 12345  # Port number

    client_socket = socket.socket()  # Create socket object
    client_socket.connect((host, port))  # Connect to server

    shift = 3  # Caesar cipher shift (same shift as the server)

    while True:
        message = input("Enter message to send to server: ")  # Get user input

        # Encrypt message using Caesar cipher
        encrypted_message = caesar_encrypt(message, shift)
        client_socket.send(encrypted_message.encode())  # Send encrypted message to server
        
        data = client_socket.recv(1024).decode()  # Receive response from server
        print("Server:", data)

        if message.lower() == "exit":
            break  # Exit the loop if 'exit' message is sent

    client_socket.close()  # Close the connection

if __name__ == '__main__':
    client_program()
