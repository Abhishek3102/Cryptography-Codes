import socket
import time

pt = input("Plaint Text: ")
keys = []
for i in range(len(pt)):
    k = int(input(f"Key {i + 1}: "))
    keys.append(k)

lu = [65, 97]

ct = ""
for i in range(len(pt)):
    ct += chr(((ord(pt[i]) - lu[0 if ord(pt[i]) < 97 else 1] + keys[i]) % 26) + lu[0 if ord(pt[i]) < 97 else 1])
    # x = ord(pt[i])
    # x -= lu[0 if x < 97 else 1]
    # x = (x + keys[i]) % 26
    # x += lu[0 if ord(pt[i]) < 97 else 1]
    # ct += chr(x)
print(ct)

kstr = ""
for k in keys:
    kstr += str(k)
    kstr += " "
print(kstr)

s = socket.socket()
port = 12345
s.bind(("", port))
s.listen(5)
c, addr = s.accept()

c.send(ct.encode())
time.sleep(10)
c.send(kstr.encode())

s.close()