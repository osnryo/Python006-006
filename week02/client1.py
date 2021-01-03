# import requests
# # pip3 install requests

# r = requests.get('http://www.httpbin.org')
# print(r.status_code) 
# print(r.headers)
# # print(r.text)


#!/usr/bin/env python
import socket
# AF_INET IPv4地址 ， SOCK_STREAM TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# debug
print(f"s1 : {s}")

s.connect(('www.httpbin.org', 80))

# debug
print(f"s2 : {s}")

s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n')

buffer = []

while True:
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break

s.close()

response = b''.join(buffer)

header, html = response.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

with open('index.html', 'wb') as f:
    f.write(html)
