import socket

# Define server host and port
host = '127.0.0.1'  # localhost
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on ", host,":", port)

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from {}:{}".format(client_address[0], client_address[1]))

    # Receive data from the client
    height = float(client_socket.recv(1024).decode())
    weight = float(client_socket.recv(1024).decode())

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Send the BMI back to the client
    client_socket.send(str(bmi).encode())

    # Close the client socket
    client_socket.close()