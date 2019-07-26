"""
1.导入模块
2.创建套接字
3.设置地址重用
4.绑定端口
5.设置监听,让套接字由主动变为被动接收
6.接收客户端发来的连接请求，定义函数request_handler()
7.接收客户端发来的协议
8.判断协议是否为空
9.拼接响应报文
10.发送响应报文
11.关闭与此客户端的连接
"""
import socket




def request_handler(client_connectionrequest_socket,client_connectionrequest_ipport):
    """接收信息，并作出响应"""
    #接收客户端发来的请求协议
    request_data = client_connectionrequest_socket.recv(1024)
    print(request_data)
    #判断协议内容是否为空
    if not request_data:
        print("%s客户端已下线" %str(client_connectionrequest_ipport))
        client_connectionrequest_socket.close()
        return
    #拼接响应报文
    #响应行，响应头，响应空行，响应内容
    response_line = "HTTP/1.1 200 OK \r\n"
    response_head = "Server:Python2.0ws/2.1 \r\n"
    response_blankline = "\r\n"
    response_body = "Hello World"
    response_data = response_line + response_head + response_blankline + response_body
    #发送响应报文
    client_connectionrequest_socket.send(request_data.encode())

    #关闭连接
    client_connectionrequest_socket.close()
def main():
    """主函数"""

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #设置地址重用
    #                          level：当前套接字    optname:地址重用  可以重用
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    server_socket.bind(("",8080))

    #设置监听，128是最大允许连接数
    server_socket.listen(128)

    #接收客户端发来的连接请求
    while True:
        client_connectionrequest_socket,client_connectionrequest_ipport = server_socket.accept()
        #在函数里接收请求
        request_handler(client_connectionrequest_socket,client_connectionrequest_ipport)

    server_socket.close()

if __name__ == '__main__':

    main()