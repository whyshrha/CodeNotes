# Github学生优惠

Digitocean：通过https://education.github.com/pack/offers 获取学生优惠，注册后点击下面的  

Digitocean 获取Your code 优惠码。 

之后Create Droplets（create cloud serves） 

系统Cent OS — Standard $5/mo — datacenter(San Francisco)  — additional options(ipv6) —  

Add your ssh key(也可不加)



1. `$ yum install wget`      安装wget命令
2. `$ wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && ./bbr.sh`     安装加速配置，(可以不加)。
3. `$ reboot`   重启
4. `$ wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh`  安装shadowsocks
5. `$ chmod +x shadowsocks-all.sh`    更改让sh成为可执行文件
6. `$ ./shadowsocks-all.sh`     运行进行配置。加密方式建议aes-256-gcm等，不建议cfb或rc4。
7. 如果想配置ipv6，则修改 `vi /etc/shadowsocks-python/config.json`文件，Ipv6 将配置中的“0.0.0.0” 改为 "::”。之后需要重启shadowsocks，`/etc/init.d/shadowsocks-python restart`。





# 下载shadowsocks客户端

1. mac windows 直接google shadowsocks download
2. android 直接电脑下载 然后传到手机，进行安装。
3. IOS，推荐ConnectSPro？



# 安装shadowsocks

Terminal安装参考：[链接]([https://medium.com/@jackme256/%E6%90%AC%E7%93%A6%E5%B7%A5-vps-%E6%90%AD%E5%BB%BA-shadowsocks-ss-%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91%E5%9B%BE%E6%96%87%E6%95%99%E7%A8%8B-ss%E5%A4%9A%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE%E4%BC%98%E5%8C%96-efc6dda704fe](https://medium.com/@jackme256/搬瓦工-vps-搭建-shadowsocks-ss-科学上网图文教程-ss多用户配置优化-efc6dda704fe))。







# References

digitalocean更换IP，参照https://www.4spaces.org/digitalocean-change-region/

Ipv6 参照： [https://www.polarxiong.com/archives/%E6%90%AD%E5%BB%BAipv6-VPN-%E8%AE%A9ipv4%E4%B8%8Aipv6-%E4%B8%8B%E8%BD%BD%E9%80%9F%E5%BA%A6%E6%8F%90%E5%8D%87%E5%88%B0100M.html](https://www.polarxiong.com/archives/搭建ipv6-VPN-让ipv4上ipv6-下载速度提升到100M.html)

bbs参照：https://bbs.pku.edu.cn/v2/post-read.php?bid=35&threadid=16378830



# 附录

1.查询 ssh key 

Mac: `$cd .ssh`  `$cat id_rsa.pub` 



2.Vi使用介绍 https://www.jianshu.com/p/bcbe916f97e1 

三种模式：编辑模式、插入模式、命令模式 

进入后按i 进入编辑模式，之后ESC退出编辑模式，输入“：” wq为保存退出，q！为不保存退出。 



3.其他服务器，目前整理的可用途径： 

1. 搬瓦工 https://bandwagonhost.com/  
2. Digitocean https://cloud.digitalocean.com  
3. 谷歌云 参照 https://bbs.pku.edu.cn/v2/post-read.php?bid=35&threadid=16378830 
4. Vultr 参照 https://bbs.pku.edu.cn/v2/post-read.php?bid=35&threadid=16979457 

