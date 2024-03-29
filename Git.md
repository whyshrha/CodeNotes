[TOC]

# Git命令

---
## 安装Git

[官方介绍](<https://git-scm.com/book/en/v2>)



## Git 基本操作

### 创建仓库

1. 本地创建版本库，在你需要的文件夹下 $`git init`
2. 或者从存在版本库中clone  $`git clone github_address`

### 仓库状态

查看文件状态 $git status

Untracked文件是未在Git中的文件，Tracked文件是在Git中的文件。在Git文件中，原始的称为Unmodified，修改后称为Modified。顺序为需要将修改的文件add到Staged状态，然后commit到Unmodified状态。

通俗的讲，文件修改后，先需要add，然后需要commit。

1. add的使用方法 $`git add <file_name>`
2. commit的使用方法 $`git commit -m <"annotation">`
3. 查看文件所处状态 $`git status`

### 版本控制查看

版本控制查看每次都做了什么修改，为阶段性提交就好，也就是历史记录。版本退回方法。

1. 查看详细历史记录 $`git log`
2. 查看简单历史记录 $`git log --pretty=oneline`
3. 版本退回到上一个版本 $`git reset --hard HEAD^`
4. 版本退回到指定版本 $`git reset --hard <commit id>`
5. 查看命令的历史记录，确定回到哪个版本 $`git reflog`

### 撤销修改

*注意：这里的 “—” 一定要有，否则为切换分支的命令*

当修改了文件，还没有add的时候，可以用撤回 $`git checkout -- <file_name>`

当add后，又做了修改，撤回到add的状态，可以用$`git checkout -- <file_name>`

当add后，想撤回到add之前的状态，可以用$`git reset HEAD <file_name>`

### 删除文件

一般在文件管理器中删除，$`rm <file_name>`

还需要在版本库中删除该文件$`git rm <file_name>`

不小心误删，可以用$`git checkout -- <file_name>`撤回

## 远程仓库

需要先将本机的SSH Key添加到Github中，使得本地Git仓库和Github仓库锥尖传输可以通过SSH加密。本机创建SSH Key，获取id_rsa.pub公钥。在Github的Account settings上Add SSH Key。

部分内容可以参考[廖雪峰Git](https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416)。


对于Mac用户，可以
1. 查看密钥是否存在
	
打开终端查看是否存在SSH密钥： `cd ~/.ssh`
没有文件，就是没有。

2. 如果没有生成新的密钥

`ssh-keygen -t rsa -C "youremail@example.com"`
之后一路回车即可。

进入rsa.pub 复制它，到Github中即可。


关于其中遇到的问题，亦可参考https://cloud.tencent.com/developer/article/1861466


### Github

从Github克隆到本地，建议先Fork，以后可以本地同步远程（远程仓库名字为origin）。或者在Github上先建立一个空的仓库。

1. 将本地仓库与Github仓库关联		$`git remote add origin git@github.com:your_name/program_name.git`

复制的时候，记得用**Git协议的，即上面格式的**，不要用http协议的，否则git push 会报错，无法通信。


2. 将本地库所有内容推送到远程库中，-u是关联主支分支		$`git push -u origin master`
3. 之后的提交就可以直接用 $`git push origin master`

### 标签管理

1. 为版本打上标签 $`git tag v1.0`
2. 查看所有标签 $`git tag`
3. 如果忘记打标签，可以先查找commit历史记录 $`git log --pretty=oneline --abbrev-commit`
4. 根据查找到的commit id进行打标签 $`git tag v0.9 <commit id>`
5. 查看标签信息 $`git show v0.9`
6. 创建带有说明的标签 -a是指定标签名，-m是指定说明文字$`git tag -a v0.1 -m "<describtion information>" <commit id>`
7. 如果标签打错了，删除$`git tag -d v0.1`
8. **如果推送某个标签到远程，可以使用$`git push origin <tagname>`**
9. 如果删除远程的标签，则需要先删除本地$`git tag -d <tagname>` ，然后远程删除`git push origin :refs/tags/<tagname>`

### 解决分支冲突问题

1. git 提交冲突的解决方法【多人协作，版本提交冲突】：

   `$ git pull --rebase`

2. push前先将远程repository修改pull下来【创建新的，远程加了ReadMe，导致本地远程冲突】

   $ git pull origin master （若还是不行，git pull origin master --allow-unrelated-histories）

   $ git push -u origin master

   重新建立时候，用git clone创建文件可以避免；远程不加ReadMe可以避免。

3. 使用强制push的方法：

   $ git push -u origin master -f 

   这样会使远程修改丢失，一般是不可取的，尤其是多人协作开发的时候。





### 清除.DS_Store

remote delete .DS_Store

```
git rm --cached .DS_Store
git commit -m 'delete .DS_Store'
touch .gitignore
vim .gitignore
```

insert

.DS_Store

*/.DS_Store











