import socket

s = socket.socket()
port = 12345
s.connect(("127.0.0.1", port))

ct = s.recv(1024).decode()
kstr = s.recv(1024).decode()

keys = []
x = ""
for l in kstr:
    if l == " ":
        keys.append(int(x))
        x = ""
        continue
    x += l

lu = [65, 97]

pt = ""
for i in range(len(ct)):
    x = ord(ct[i])
    x -= lu[0 if ord(ct[i]) < 97 else 1]
    x = (x + 26 - keys[i]) % 26
    x += lu[0 if ord(ct[i]) < 97 else 1]
    pt += chr(x)

print(f"Plaint Text: {pt}")

s.close()
