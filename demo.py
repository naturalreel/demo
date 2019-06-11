import socket

def service_client(new_socket):
    """为这个客户端返回数据"""
    #1.接收游览器发送过来的请求,即http
    #GET/HTTP/1.1
    #...
    request=new_socket.recv(1024)
    print(request)
    #2.返回http格式的数据.给游览器
    response="HTTP/1.1 200 OK \r\n"
    response+="\r\n"
    #2.1准备发送给游览器的数据---boy
    response+="<h1>hh</h1>"
    new_socket.send(response.encode("utf-8"))
    #关闭套接字
    new_socket.close()
def main():
    """用来完成整体的控制"""
    #1.创建套接字
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2.绑定
    tcp_server_socket.bind(("",7890))
    #3.监听套接字
    tcp_server_socket.listen(128)
    while True:
        #4.等待新客户端的连接
        new_socket,client_addr=tcp_server_socket.accept()
        #5.为这个客户端服务
        service_client(new_socket)
    #关闭监听套接字
    tcp_server_socket.close()
if __name__=="__main__":
    main()