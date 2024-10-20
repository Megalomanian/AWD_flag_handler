import socket  
import request
def submit_flag(flag):
    url2 = 'http://10.233.*.*:801/flag_file.php?token=team3&flag=%s' %flag
    submit = request.get(url2).text
    print(submit)
def start_server(host, port):  
    # 创建一个TCP/IP套接字  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:  
        # 绑定套接字到指定的地址和端口  
        server_socket.bind((host, port))  
        # 开始监听传入连接  
        server_socket.listen()  
        print(f"Server listening on {host}:{port}")  
  
        while True:  
            # 等待连接  
            client_socket, client_address = server_socket.accept()  
            with client_socket:  
                print(f"Connected by {client_address}")  
                while True:  
                    # 接收数据  
                    data = client_socket.recv(1024)  
                    if not data:  
                        break  # 连接关闭  
                    # 打印接收到的数据  
                    print(f"Received: {data.decode()}") 
                    flag = str(data.decode())
                    try:
                        submit_flag(flag)
                        print("flag submitted successfully")
                    except:
                        print("fail to submit flag")

if __name__ == "__main__":  
    HOST = '127.0.0.1'  # 监听的主机地址  
    PORT = 12346       # 监听的端口号  
    start_server(HOST, PORT)
