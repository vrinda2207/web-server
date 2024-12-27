import socket
host='localhost'
port=5555
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(5)
while True:
    client_Socket,client_address=server_socket.accept()
    print(f"connection from {client_address}")
    req=client_Socket.recv(1024).decode()
    print(f"request={req}")
    response="""/http/1.1  200 OK
    Content-Type=text/HTML
    <html>
    <head><title>simple web server</title></head>
    <body><h1>WELCOME </h1></body>
    </html>
    """
    client_Socket.sendall(response.encode())
    client_Socket.close()
              
