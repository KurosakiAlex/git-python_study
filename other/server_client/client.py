import socket

client = socket.socket()
client.connect(('127.0.0.1', 8080))

while True:
    client.send(b'hello world')  # 发送数据给server方
    data = client.recv(1024)  # 接收数据
    print(data)



