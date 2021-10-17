# 服务器初次使用

1. 登陆 `ssh username@ip`，之后按照提示输入密码

2. 如果服务器未安装`ssh`，需要安装ssh服务，命令为`sudo apt-get install openssh-server`

   

# 配置免密登陆

## Mac & Linux

1. 本地Mac or Linux 在Terminal上输入 `ssh-keygen` 创建公钥和私钥，之后一直回车。
2. 本地然后输入`ssh-copy-id [被控制的用户名]@[它的ip]`，完成免密登陆。

## Windows

1.下载MobaXterm，安装Portable edition，之后左上方有quick connection，输入ip地址，连接服务器。



## 创建软链

1. 即Linux中的快捷方式，当服务器ssd盘较小时，需要使用软链。
   * ln -s 源地址 目的地址 e.g.  `ln -s ./python/bin/python3.6 ./python3`

## 进行加密压缩

压缩 `$zip -re filename.zip filename`  回车后，输入两次密码

解压缩 `$unzip filename.zip` 按提示输入密码


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






# 服务器与移动硬盘之间的数据传输

记录服务器和移动硬盘之间的数据传输方法。从未进机房的小白进行方法的记录。

服务器由于种种原因不能联网，数据又都在服务器上，这时只能手动将服务器上的数据拷贝下来。

大致处理方法如下：需要先将移动硬盘挂载，然后scp传输，然后解除挂载。

1. 利用root账号登陆服务器，现在mnt目录下面建立一个文件夹，例如叫做usb，$`mkdir usb` 目的是这个文件夹放挂载硬盘。
2. 利用 $`fdisk -l` 查看硬盘是否被检测到，例如你发现是 Disk /dev/sdc  最后一行还有/dev/sdc1
3. 进行硬盘挂载 $`mount /dev/sdc1 /mnt/usb`
4. $`df -h` 可以查看是否挂载成功
5. $`scp -r 原始路径 目标路径` 进行文件传输
6. 解除文件挂载 $`umount /mnt/usb` 

