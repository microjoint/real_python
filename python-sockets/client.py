import socket

HOST = "127.0.0.1"
PORT = 64123

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"how ya doin'")
    data = s.recv(1024)


print(f"Received {data!r}")
