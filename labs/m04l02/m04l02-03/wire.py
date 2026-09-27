# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l02 — Data States: Security at Rest, in Transit, and in Use
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l02
# © LearnSome.tech
import base64, socket, threading
server = socket.create_server(("127.0.0.1", 0))
port = server.getsockname()[1]
def client():  # a reporting job calling an internal API over plain HTTP
    creds = base64.b64encode(b"svc-report:not-a-real-password").decode()
    body = '{"customer": "alice@example.com"}'
    with socket.create_connection(("127.0.0.1", port)) as c:
        c.sendall(("POST /v1/export HTTP/1.1\r\nHost: api.example.com\r\n"
                   f"Authorization: Basic {creds}\r\n"
                   f"Content-Length: {len(body)}\r\n\r\n{body}").encode())
threading.Thread(target=client).start()
conn, _ = server.accept()
wire = b""
while chunk := conn.recv(4096):
    wire += chunk
lines = wire.decode().split("\r\n")
for line in lines:
    print("wire:", line)
auth = next(l for l in lines if l.startswith("Authorization"))
print("decoded:", base64.b64decode(auth.split()[-1]).decode())
