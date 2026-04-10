import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect(('127.0.0.1', 5000))
print("Connected!")

while True:
    
    message = input("client ")
    client_socket.send(message.encode('utf-8'))
    if message.lower() == 'exit':
        break
    
    
    data = client_socket.recv(1024).decode('utf-8')
    if not data or data.lower() == 'exit':
        break
    print(f"server: {data}")

client_socket.close()