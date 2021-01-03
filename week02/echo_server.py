import socket

HOST = 'localhost'
PORT = 9000
Filename = 'test_server.log'

def echo_server() :

    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    # 把对象s绑定到指定的服务端口
    s.bind((HOST , PORT))
    # 设置接收链接数
    s.listen(1)
    while True :
        # accep表示接收用户端的链接
        conn , addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')

        while True :
            data = conn.recv(1024)
            if not data :
                break
            #conn.sendall(data)
            with open(Filename,'w') as p :
                p.write(data.decode('utf-8'))

        conn.close()
    
    s.close()

if __name__ == '__main__' :
    echo_server()