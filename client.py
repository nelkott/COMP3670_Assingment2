import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
CLIENT_NUM = None

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))
    except  socket.error as e:
        print(str(e))
        
    Response = client.recv(1024)
    if Response.decode('utf-8')[:3] == "220":
        CLIENT_NUM = Response.decode('utf-8')[-1]
        print("Client #" + str(CLIENT_NUM) + " Welcome to the Server")
    else:
        print("Server is not ready please try again")
        
    while True:
        command = input("Enter your command type \help for help: ")
        if command == "QUIT":
            client.sendall(str.encode(command))
            sys.exit()
        
        elif command == "REQUEST JOB":
            print("HI")
            client.sendall(str.encode(command))
        
        elif command == "\help":
            print("""Commands Avaliable: 
                  ========================
                  \help - for help
                  QUIT - to QUIT the program
                  REQUEST JOB - request a job from job creator""")
            continue
            
            
        Response = client.recv(1024)
        
        if Response.decode('utf-8') == "250":
            print("Client #" + str(CLIENT_NUM) + " Job recieved")
            
        elif Response.decode('utf-8') == '452':
            print("Client #" + str(CLIENT_NUM) + " you already haave a job taken")
        
        
        print(Response.decode('utf-8'))
    client.close()