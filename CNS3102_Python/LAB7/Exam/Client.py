import socket

# Define server host and port
host = '127.0.0.1'  # localhost
port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Get user input for height and weight
height = input("Enter your height (in meters): ")
weight = input("Enter your weight (in kilograms): ")

# Send height and weight to the server
client_socket.send(height.encode())
client_socket.send(weight.encode())

# Receive the BMI from the server
bmi = float(client_socket.recv(1024).decode())

# Print the result
print("Your BMI is: ", round(bmi,2))

# Close the client socket
client_socket.close()