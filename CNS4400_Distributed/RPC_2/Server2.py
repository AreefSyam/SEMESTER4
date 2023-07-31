from xmlrpc.server import SimpleXMLRPCServer

# initialize the chunks list
chunks = []

def receive_chunk(chunk):
    # append the chunk to the global list
    global chunks
    chunks.append(chunk)

def reassemble_message():
    # concatenate the chunks into the original message
    global chunks
    return ''.join(chunks)

# create a SimpleXMLRPCServer and register the receive_chunk and reassemble_message methods with it
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_function(receive_chunk, "receive_chunk")
server.register_function(reassemble_message, "reassemble_message")

# start the server and wait for incoming requests
server.serve_forever()
