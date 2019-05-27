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
*   user
:   表示终端数量  
*   load average
:   表示1，5，15分钟的负载情况  
*   PID
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
## 文件目录管理
*   `touch`
:   创建文件，带参-a表示修改atime,-m表示修改mtime,-d表示同时修改atime和mtime  
*   `mkdir -p a/b/c/d/e`
:   创建带有嵌套关系的目录 -p
*   `cp`
:   复制 -r用于操作目录
*   `mv`
:   用于剪切或者重命名，如果在同一个目录中对一个文件进行剪切操作，其实也就是对其进行重命名  
*   `rm`
:   删除，-f表示强制删除，如果没用-f参数则需要询问y/n ,-r表示目录操作  
*   `dd`
:   if(inputfile),of(outfile),bs(块的大小),count(多少块)，如dd if=a.txt of=b.txt bs=80 count=1
*   `file`
:   查看文件类型  
## 打包压缩与搜索
*   `tar Options 压缩包  源文件`  

*   Options

    -c	创建压缩文件  
    -x	解开压缩文件  
    -t	查看压缩包内有哪些文件  
    -z	用Gzip压缩或解压  
    -j	用bzip2压缩或解压  
    -v	显示压缩或解压的过程  
    -f	目标文件名  
    -p	保留原始的权限与属性  
    -P	使用绝对路径来压缩  
    -C	指定解压到的目录  
    cjvf  使用bz2打包压缩,得到.tar.bz2
    czvf  使用gzip打包压缩,得到.tar.gz
    
*   `grep 关键字 文件`
:   比配文件中有包含关键字的内容
*   `find / -name filename`
:   找到当前目录下文件名为filename的文件  
*   `find / -path 忽略目录 -prune -name filename`
:   找到当前目录下忽略某目录中文件名为filename的文件

    -name	匹配名称  
    -perm	匹配权限（mode为完全匹配，-mode为包含即可）  
    -user	匹配所有者  
    -group	匹配所有组  
    -mtime -n +n	匹配修改内容的时间（-n指n天以内，+n指n天以前）  
    -atime -n +n	匹配访问文件的时间（-n指n天以内，+n指n天以前）  
    -ctime -n +n	匹配修改文件权限的时间（-n指n天以内，+n指n天以前）  
    -nouser	匹配无所有者的文件  
    -nogroup	匹配无所有组的文件  
    -newer f1 !f2	匹配比文件f1新但比f2旧的文件  
    --type b/d/c/p/l/f	匹配文件类型（后面的字幕字母依次表示块设备、目录、字符设备、管道、链接文件、文本文件）  
    -size	匹配文件的大小（+50KB为查找超过50KB的文件，而-50KB为查找小于50KB的文件）  
    -prune	忽略某个目录  
    -exec …… {}\;	后面可跟用于进一步处理搜索结果的命令（下文会有演示）  
*   `find / -user freax -exec cp -a {} /root/findresults/ \;` 
:   整个文件系统中找出所有归属于freax用户的文件并复制到/root/findresults目录  

## 输入输出重定向
*  '>' 文件	将标准输出重定向到一个文件中（清空原有文件的数据）  
    命令 2> 文件	将错误输出重定向到一个文件中（清空原有文件的数据）  
    命令 >> 文件	将标准输出重定向到一个文件中（追加到原有内容的后面）  
    命令 2>> 文件	将错误输出重定向到一个文件中（追加到原有内容的后面）  
    命令 >> 文件 2>&1   
    或命令 &>> 文件  

    命令 < 文件	将文件作为命令的标准输入  
    命令 << 分界符	从标准输入中读入，直到遇见分界符才停止  
    命令 < 文件1 > 文件2	将文件1作为命令的标准输入并将标准输出到文件2  

## 管道符 
*   `命令A | 命令B`
:   将命令A的结果作为命令B的输入，比如统计当前目录下的文件数`ls | wc -l`

## 通配符 * ？

## 常用的转义符 $ \ "" '' ``
*   `PRICE=5`  
*   `echo Price is \$$PRICE`  
*   `echo 'Price is \$$PRICE'` 
:   整体转义
  
```
    echo `uname -a`:   执行命令  
```


     



 

    











  

