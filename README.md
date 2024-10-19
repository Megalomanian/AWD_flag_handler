# 欢迎使用鑫启网安AWD自动获取flag工具
### 环境准备
首先，确保你的系统为linux的某种发行版
以ubuntu为例
通过以下命令安装python3
```sh
sudo apt-get install python3
```
通过以下命令安装gcc
```sh
sudo apt install build-essential
```
### 用法
首先，确保拿到对方的shell权限
在本地攻击机环境下运行以下命令，以开始tcp监听
```sh
python3 flag_handler.py
```
而后，在本地攻击机（linux）的环境下，使用flag_capture.py生成木马
在本地开启内网穿透，穿透12346端口（内网穿透的开启方法不做赘述）
假设在内网穿透的端口，将本地的127.0.0.1:12346穿透到111.111.111.111:2222，那么你应该以以下命令生成木马
```sh
python3 flag_capture.py 111.111.111.111 2222
```
接下来，在根目录下，你会得到一个名为时间戳的文件
将此文件上传至已取得shell权限的靶机，而后运行，即可在flag_handler.py的shell中自动获取flag
注：当前版本还不能全自动提交flag，等我下次打AWD的时候去抓个包看看怎么改request