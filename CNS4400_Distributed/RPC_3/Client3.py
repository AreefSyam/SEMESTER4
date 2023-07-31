import socket

class RPCClient:
    def __init__(self, host, port):
        # 1 : create a connection to server
        self.sock = socket.create_connection((host, port))
        
    def call(self, method, *args):
        # 2: send the 'method name' and 'arguments/parameter' to the server
        self.sock.sendall(f"{method},{','.join(args)}\n".encode())
        
        # 3: receive the result from the server and return it
        result = self.sock.recv(1024).strip().decode()
        if result.startswith("Error:"):
            raise Exception(result)
        return result

# create an instance of the RPCClient class and call some functions on the server
client = RPCClient('localhost', 8000)
print(client.call('add', '1', '2'))
print(client.call('subtract', '3', '4'))
print(client.call('multiply','20','2'))
print(client.call('divide','20','2'))