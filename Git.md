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

### Github

从Github克隆到本地，建议先Fork，以后可以本地同步远程（远程仓库名字为origin）。或者在Github上先建立一个空的仓库。

1. 将本地仓库与Github仓库关联		$`git remote add origin git@github.com:your_name/program_name.git`
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













