[TOC]

# Git命令

---
## 安装Git

[官方介绍](<https://git-scm.com/book/en/v2>)



## Git 基本操作

### 创建仓库

1. 本地创建版本库，在你需要的文件夹下 $git init
2. 或者从存在版本库中clone  $git clone github_address

### 仓库状态

查看文件状态 $git status

Untracked文件是未在Git中的文件，Tracked文件是在Git中的文件。在Git文件中，原始的称为Unmodified，修改后称为Modified。顺序为需要将修改的文件add到Staged状态，然后commit到Unmodified状态。

通俗的讲，文件修改后，先需要add，然后需要commit。



### Github

从Github克隆到本地，建议先Fork，以后可以本地同步远程（远程仓库名字为origin）

将本地仓库与Github仓库关联		$git remote add origin git@github.com:your_name/program_name.git

将本地库所有内容推送到远程库中		$git push -u origin master









