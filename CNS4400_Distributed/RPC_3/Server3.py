import socketserver

# define the request handler class for handling client requests
class RPCHandler(socketserver.StreamRequestHandler):

    # handle method is called when a client connects to the server
    def handle(self):
        while True:
            # 1: receive the data from the client
            data = self.rfile.readline().strip().decode()
            if not data:
                break
            
            # 2: parse the method name and arguments
            method, *args = data.split(",")
            print(method) # just checking
            
            # call the appropriate function on the server and send the result back to the client
            try:
                # 3 : call the function with the given method name and arguments
                result = str(getattr(self.server, method)(*args))
            except Exception as e:
                # if an exception occurs, send an error message back to the client
                result = f"Error: {str(e)}"

            # 4 : send the result back to the client
            # self.wfile.write(method.encode() + b":\t" + result.encode() + b"\n")
            self.wfile.write("{:<10}\t{}\n".format(method+":", result).encode()) #good output


# define the TCP server class that uses the request handler class
class RPCServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass



from threading import Thread

# create an instance of the RPCServer class and register some functions
server = RPCServer(('localhost', 8000), RPCHandler)
server.add = lambda x, y: int(x) + int(y)
server.subtract = lambda x, y: int(x) - int(y)
server.multiply = lambda x, y: int(x) * int(y)
server.divide = lambda x, y: int(x) / int(y)

# start the server in a separate thread
def start_server():
    server.serve_forever()

server_thread = Thread(target=start_server)
server_thread.start()

# check if the server is running
if server_thread.is_alive():
    print("Success Connect")
else:
    print("Connection Failed")







