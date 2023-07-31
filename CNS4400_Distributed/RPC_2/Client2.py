import xmlrpc.client

# create an XML-RPC proxy to the remote server
server = xmlrpc.client.ServerProxy("http://localhost:8000", allow_none=True)

# define the message to send
message = "This is a long message that needs to be sent over RPC."

# set the chunk size
chunk_size = 10

# loop through the message in chunks and send them one at a time
try:
    for i in range(0, len(message), chunk_size):
        chunk = message[i:i+chunk_size]
        if chunk:
            server.receive_chunk(chunk)
except Exception as e:
    print(f"An error occurred: {e}")
else:
    # call the reassemble_message() method to get the final message
    final_message = server.reassemble_message()
    print(f"Final message: {final_message}")
