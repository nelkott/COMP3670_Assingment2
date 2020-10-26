import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))
    except  socket.error as e:
        print(str(e))
        
    Response = client.recv(1024)
    print(Response.decode('utf-8'))
    while True:
        command = input("SAY something: ")
        if command == "QUIT":
            client.sendall(str.encode(command))
            import sys
            sys.exit()
        client.sendall(str.encode(command))
        Response = client.recv(1024)
        print(Response.decode('utf-8'))
    client.close()