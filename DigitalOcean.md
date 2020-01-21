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





# 下载shadowsocksR客户端

1. Mac 下载https://github.com/qinyuhang/ShadowsocksX-NG-R/releases 

2. Windows下载https://github.com/shadowsocksrr/shadowsocksr-csharp/releases 下载v4.9.0

3. android 下载 https://github.com/shadowsocksrr/shadowsocksr-android/releases 

4. IOS，搜索Mume(暮梅)、Potatso Lite、FastSocks、Shadowrocket 

   https://shadowsockshelp.github.io/Shadowsocks/ios.html 苹果 iOS 使用 Shadowsocks 设置教程

   https://tlanyan.me/get-proxy-clients/ ios科学上网

   













# 安装shadowsocksR

Terminal安装参考：[链接]([https://medium.com/@jackme256/%E6%90%AC%E7%93%A6%E5%B7%A5-vps-%E6%90%AD%E5%BB%BA-shadowsocks-ss-%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91%E5%9B%BE%E6%96%87%E6%95%99%E7%A8%8B-ss%E5%A4%9A%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE%E4%BC%98%E5%8C%96-efc6dda704fe])。需科学上网。

### 最新版方法

1.打开Mac终端，登陆VPS

`ssh -p 端口号 root@ip`

2.默认系统为Centos 6 x86

**ShadowsocksR配置**

* 安装wegt工具

  `yum install wget`

* 下载ssR

  ```
  wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocksR.sh
  ```

* 把下载的ssR变成可以执行的

  `chmod +x shadowsocksR.sh`

* 执行ssR

  `./shadowsocksR.sh 2>&1 | tee shadowsocksR.log`

* 如果日后需要修改配置

  `启动：/etc/init.d/shadowsocks start`

  `停止：/etc/init.d/shadowsocks `

  `stop重启：/etc/init.d/shadowsocks `

  `restart状态：/etc/init.d/shadowsocks `

  `status配置文件路径：/etc/shadowsocks.json`

  `日志文件路径：/var/log/shadowsocks.log`

  `代码安装目录：/usr/local/shadowsocks`

* 如需卸载

  ```
  ./shadowsocksR.sh uninstall
  ```





**Shadowsocks配置**

 * 安装wegt工具

   `yum install wget`

 * 下载ss

   `wget — no-check-certificate -O shadowsocks.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh`

* 把下载的ss变成可以执行的

  `chmod +x shadowsocks.sh`

* 执行ss

  `./shadowsocks.sh 2>&1 | tee shadowsocks.log`

* 如果日后需要修改配置

  * 进入json

    `vi /etc/shadowsocks.json`

  * 重启ss

    `/etc/init.d/shadowsocks restart`

  * 关闭防火墙（这个可以不管）

    `service iptables stop`

    `chkconfig iptables off`

    







# References

digitalocean更换IP，参照https://www.4spaces.org/digitalocean-change-region/

Ipv6 参照： [https://www.polarxiong.com/archives/%E6%90%AD%E5%BB%BAipv6-VPN-%E8%AE%A9ipv4%E4%B8%8Aipv6-%E4%B8%8B%E8%BD%BD%E9%80%9F%E5%BA%A6%E6%8F%90%E5%8D%87%E5%88%B0100M.html](https://www.polarxiong.com/archives/搭建ipv6-VPN-让ipv4上ipv6-下载速度提升到100M.html)

bbs参照（Google云）：https://bbs.pku.edu.cn/v2/post-read.php?bid=35&threadid=16378830

shadowsocksR一键安装：http://www.wangchao.info/1549.html?nsukey=EXVQ%2BS5%2FoTUmz2Ool8KDfM9cFu%2BQafBZVbR6h135Qy5g%2BWPzmpXovkXl5tild%2BeEPrynn40KsoJ7%2FZZD8ndAVBDLaZjx4zB3gi6FSpY8flOCfJeVSciD5DtWNYCKX9S%2FpzeNEq0bxN5xZK%2BeHSDeXIREbjQcagBt8KtKbyVBS2MnuljMRu9SGhw5f8HLi6xrMaQx1gzVeLczQBwlowCkuw%3D%3D























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

5. 多个端口模板

   "server":"::",
       "local_address":"127.0.0.1",
       "local_port":1080,
       "port_password":{
   	"9000":"why123456",
   	"9001":"why123456",
   	"9002":"why123456"
       },
       "timeout":300,
       "method":"aes-256-gcm",
       "fast_open":true

