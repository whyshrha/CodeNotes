# 服务器初次使用

1. 登陆 `ssh username@ip`，之后按照提示输入密码

2. 如果服务器未安装`ssh`，需要安装ssh服务，命令为`sudo apt-get install openssh-server`

   

# 配置免密登陆

## Mac & Linux

1. Mac or Linux 在Terminal上输入 `ssh-keygen` 创建公钥和私钥，之后一直回车。
2. 然后输入`ssh-copy-id [被控制的用户名]@[它的ip]`，完成免密登陆。

## Windows

1.下载MobaXterm，安装Portable edition，之后左上方有quick connection，输入ip地址，连接服务器。



## 创建软链

1. 即Linux中的快捷方式，当服务器ssd盘较小时，需要使用软链。
   * ln -s 源地址 目的地址 e.g.  `ln -s ./python/bin/python3.6 ./python3`



# 安装Anaconda

1. 输入`wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh`，下载Anaconda。
2. 输入`bash Anaconda3-5.3.1-Linux-x86_64.sh`。
3. 安装完后，记得重新进入一下。

# 打开jupyter lab

1. 输入`jupyter-lab --ip=0.0.0.0 --no-browser --port=7966 1>tmp.log 2>&1 &`
2. 本地输入`ssh -L 8900:localhost:7966 wuhaoyu@112.126.102.160`
3. 本地浏览器输入`http://localhost:8900`



## 查询Token

在远程服务器上，输入`jupyter notebook list`，即可查询Token。



# WOE学习

