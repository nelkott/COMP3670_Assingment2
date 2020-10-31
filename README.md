# COMP3670_Assingment2
Members: Nidhi Patel, Nour Elkott, Salwa Mohamed, Niraj Patel

# Server-Side Design
- A server has 2 steps in order to begin the server and wait for connections.
    - 1) code bind() and listen() are the function calls that begin the server.
        -The bind() command attaches the socket to a port
        - listen() command tells the interface to prepare to queue incoming connection requests
    - 2) after the server has been set to listen, a call must be made which waits for a client to try to connect.
        - This call is ideal to call this in a thread to allow the connection to be accepted, a new file descriptor is returned.
    - The function written here returns a new socket when the connection is accepted, created from the file descriptor returned by the accept function. In order for this to work a constructor must be created that will accept a file descriptor.
- The socket waiting for connections can be closed if only one connection is expected, or left open to allow multiple clients to connect simultaneously
- The function written here returns a new socket when the connection is accepted, created from the file descriptor returned by the accept function. In order for this to work a constructor must be created that will accept a file descriptor.

# Client-Side Design
- Only one call is needed to be made before the socket can use read and write.
    - Called connect: requires the IP address and port number of the server it needs to connect to.
    - Allows the client to connect to a server using both an IP address or hostname.
- If the server does not respond correctly, the socket is closed. If successful, the read and write commands can be used to transmit data.

# Common Functions
- After configuring the server or the client, the sockets will act identically and it does not matter which side either of the command functions are called from.
- Common functions:
    - read() : 
    - recv() : will copy data from the socket to the buffer
    - write() : instead of copying data from the socket to the buffer, it copies date from the buffer to the socket.

# Protocol Packet Design Pattern
- Protocol stack generally handles multiple layers of a protocol
- There are two pieces of sata needed in a packet:
    - Message type
    - Data buffer
- The message type describes what type of data will be sent to the attached data buffer.

# Implementing the Application Protocol
- We have defined the packet structure, now we have to implement the functionality of the Application Protocol (ie. writing, reading, handling different message types, etc).
- Sending a Message from the Server to the Client
    - Sent by casting
    - Message type must be defined
    - Playload data needs to be copied into the outgoing message, which is sent over the network.
- Receiving a Message by Client from Server
    - Note: when receiving message command is called, the program will be blocked until the bytes requested is received
    - The received data will be casted into the type of data expected by the server

# Need for new application layer
- Our network application protocols don't match current existing application layer protocols, so a new application layer protocol for this network would need to be.