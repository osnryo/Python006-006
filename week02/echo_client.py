import socket

HOST = 'localhost'
PORT = 9000
Filename = 'test.log'
def echo_clinet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #socket.socket fd=524, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0
    #fd x号文件描述符-0:标准输入;1标准输出:;2:错误输出；family：ipv4

    s.connect((HOST,PORT))

    while True :
        # 接受用户输入

        data_send =  input('input : ')

        # 设定退出条件
        if data_send == 'exit' :
            break 

        if not data_send :
            with open(Filename) as s :
                data =  s.read()

        # 发送数据请求
        s.sendall(data.encode())

        # 接收服务端的请求
        data_reveive = s.recv(1024)

        if not data_reveive :
            break
        else:
            print(data.decode('utf-8'))
    
    s.close()
    
if __name__ == '__main__' :
    echo_clinet()