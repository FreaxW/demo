# Git教程 

## 基本概念
>### Repository
>仓库，用来存放项目 
>### Watch
>关注，如果有更新会通知
>### Star
>收藏
>### Fork
>复制克隆至自己仓库(fork)，标识forked from
>### Issues
>发现bug
>### Pull request
>发起请求,等待别人确认是否合并merge

## 页面
>1.github主页
>2.仓库主页
>3.个人主页

## 注册github
>[github](https://github.com)  
>vpn Shadowsocks  
>还需Verify your email

## 创建一个本地仓库 
>git init

>## 本地克隆远程仓库
>cd demo   
[MyGithub](https://github.com/FreaxW/demo.git)   
>git clone  https://github.com/FreaxW/demo.git
>查看目录情况 ls -a
>cd .git

## 查看状态
>git status



>## 创建分支

>### 创建分支不切换  
>git branch newbranch

>### 创建分支并切换至该分支
>git checkout -b feature  

>## 切换分支  
>git checkout branchname

>## 添加  
>git add E:/Projects/Python/vs/demo/README.md  

## 提交需要配置用户名和邮箱地址
>git config --global user.name 'runoob'
>git config --global user.email test@runoob.com

>## 提交     
>git commit -m "代码提交信息"

>## 合并  
>提交之前必须切换回主分支git checkout master   
>git merge feature

>##  查看分支  
>git branch
>### 查看分支情况
>git branch-a
>### 查看远程分支
>git branch -r 

>## 删除分支
>必须在删除分支的上一个分支  
>git branch -d test
>### 远程删除分支
>git push origin --delete <分支名>

>## 远程更新至本地
>### 从远程获取最新到本地，不自动merge  
>git fetch
>### 从远程获取最新版本并merge到本地
>git pull

>## 回退命令
>### 回退到上个版本
>git reset --hard HEAD 
>### 回退到前3次提交之前
>git reset --hard HEAD~3
>### 回退到n次提交之前
>git reset --hard commit_id
>### 退到/进到 指定commit的sha码 
>git checkout commit ID

## 重命名本地分支，并提交到远程 
>1.重命名 git branch -m oldBranchName newBranchName    
>2.删除远程分支：git push origin :oldBranchName     
>3.将重命名过的分支提交：git push origin newBranchName    


## 说明
>### 一
>将远程仓库git cloue    
>这是master作为本地仓库的主分支  
>master创建一个分支test,并切换到该分支 git branch -b test  
>test do some changes 
>git commit -m 'message'  
>git push --set-upstream origin test   
>git merge test   
>最后远程仓库得到一个test的分支，然后compare pull,然后merge  

>### 二
>将远程仓库git cloue    
>这是master作为本地仓库的主分支  
>master do some changes  
>git commit -m 'message'  
>git push --set-upstream origin master   
>git merge master   
