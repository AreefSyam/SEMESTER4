import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")
result = server.cube(5)
print("The cube of 5 is:", result)
result = server
