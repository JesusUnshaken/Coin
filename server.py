import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind(('127.0.0.1', 5000))


server_socket.listen(1)
print("Waiting.....")

conn, addr = server_socket.accept()
print(f"Connected {addr}")

while True:
    
    data = conn.recv(1024).decode('utf-8')
    if not data or data.lower() == 'exit':
        break
    print(f"client : {data}")
    
    
    reply = input("(server): ")
    conn.send(reply.encode('utf-8'))
    if reply.lower() == 'exit':
        break

conn.close()