## linux系统进程五个状态
>R(running)
:   正在运行  
>S(sleeping
:   中断休眠  
>D(stopped)
:   不可中断，系统不响应，kill不掉  
>Z(zombie)
:   僵死  
>T
:   停止  

## 查看进程详细信息
>`ps -aux`
:   静态查看  
>`top`
:   动态查看  
*   -user
:   表示终端数量  
*   -load average
:   表示1，5，15分钟的负载情况  
*   -PID
:   进程标识，用来操作该进程,有些有多个标识，使用`killall 服务名`关闭   
>`pidofc sshd`
:   查看sshd的PID   
>`systemctl status sshd`
:   查看sshd状态  
>`kill PID`
:   关闭进程

## 系统状态检查
>`ifconfig`
:   网卡信息(Name,IP,MAC,RX,TX)查看，如果没有该命令`apt install net-tools`  
>`uname -a`
:   查看内核信息   
>`update`
:   查看负载信息  
>`free/free -h`
:   查看内存信息  
>`who`
:   查看登陆信息  
>`last`
:   登录记录  
>`history`
:   历史纪录  
*   `!序号`重复执行某个命令  
>`sosreport`
:   收集系统信息，发给服务商请求帮助

## Linux文本文件编辑
### 隐藏文件
>以点开始的文件名，比如.bashrc，可用`ls -a`查看
### 文件查看
*   `cat`
:   查看小文件
*   `more`
:   查看大小文件
*   `less`
:   查看大小文件
*   `head -n 5`
:   查看前5行
*   `tail -n 5/tail -f`
:   查看前5行/持续刷新内容
*   `tr`
:   替换文件内容，需结合使用，比如小写转大写`cat filename | tr [a-z] [A-Z]`  
*   `wc -l/-c filename`
:   统计行数/字节数
*   `stat`
:   查看件时间信息(最近访问atime,最新内容更改mtime,最新属性更改ctime) 
*   `cut -d : -f 1 `
:   提取文件中以冒号分割的第一列的信息
*   `diff --brief diff_A.txt diff_B.txt/diff -c diff_A.txt diff_B.txt`
:   判断两个文件是否相同/得到两个文件的不同点








  

