## linux终端快捷键
*   Ctrl+L
:   清空
*   Ctrl+C
:   中断
*   q
:   浏览时退出，比如`more` `man` `info`

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
>`pidof sshd`
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
>`uptime`
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
*   `find /etc -name filename`
:   找到etc目录下文件名为filename的文件  
*   `find /etc -path 忽略目录 -prune -name filename`
:   找到etc目录下忽略某目录中文件名为filename的文件

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
    echo `uname -a`:   执行命令，也可以echo $(uname -a)  
```

## 环境变量
*   PATH
*   HOME
*   SHELL
:   终端是什么
*   MAIL
:   邮件位置
*   LANG
:   系统语言  
*   RANDOM
:   随机数
*   PS1
:   Bash解释器的提示符
*   EDITOR
:   用户默认的文本编辑器
*   `type command`
:   查看变量类型，内部外部
*   `alias/unalias`
:   别名
*   `MYVAR=/home/freax`
:   变量赋值 `cd $MYVAR`
*   `export MYVAR`
:   设为全局变量，允许其他用户使用


## 编辑器vi/vim
>区别
:   vim有高亮，是vi的improve  
>常用命令
:   a i o esc :  o表示下一行
>模式
:   输入模式(esc)<->(a i o)命令模式(esc)<->(:)末行模式  
*   命令模式 
    *   dd	删除（剪切）光标所在整行  
    *   5dd	删除（剪切）从光标处开始的5行  
    *   yy	复制光标所在整行  
    *   5yy	复制从光标处开始的5行  
    *   n	显示搜索命令定位到的下一个字符串  
    *   N	显示搜索命令定位到的上一个字符串  
    *   u	撤销上一步的操作  
    *   p	将之前删除（dd）或复制（yy）过的数据粘贴到光标后面  
*   末行模式
    *   w	保存
    *   :q	退出
    *   :q!	强制退出（放弃对文档的修改内容）
    *   :wq!	强制保存退出
    *   :set nu	显示行号
    *   :set nonu	不显示行号
    *   :命令	执行该命令
    *   :整数	跳转到该行
    *   :s/one/two	将当前光标所在行的第一个one替换成two
    *   :s/one/two/g	将当前光标所在行的所有one替换成two
    *   :%s/one/two/g	将全文中的所有one替换成two
    *   ?字符串	在文本中从下至上搜索该字符串
    *   /字符串	在文本中从上至下搜索该字符串
    
## shell脚本
*   #!/bin/bash
:   指定编译器地址
*   接收参数
    *   $0
    :   文件名
    *   $#
    :   参数个数
    *   $*
    :   参数
    *   $1
    :   第一个参数
    *   $?
    :   返回0.1,判断一条命令是否成功0,1失败`[ -d /etc ] && echo "OK"`
    
*   处理参数 bash demo.sh a b c d e

*   逻辑&& ||
    *   expr1 && expr2
    :  expr1 True才会执行expr2
    *   expr1 || expr2
    :  expr1 False才会执行expr2 
*   比较
    *   eq
    :   判断相等==
    *   -ge
    :   >=
    *   -gt
    :   >
    *   -le
    :   小于
    
*   实例
    *   查看内存
    >   FreeMem=`free -m | grep Mem: | awk '{print $4}'`  
    >   [ $FreeMem -lt 1024 ] && echo "Insufficient Memory"
    *   测试变量是否是空白值
    >   [ -z $LANG ]
    *   判断是目录
    >   [ -d /etc ]
    *   判断是文件
    >   [ -f /home/freax/demo.sh ]
    *   判断文件是否存在
    >   [ -e /home/freax/demo.sh ]
    
## 条件测试
```
if expr
    then
        do something
    elif
        do something
    esle
        do something
 fi
 ```
*   `read -p "Enter:" GRADE && echo $GRADE`
:   输入

## 循环
```
for line in `cat demo.sh`
    do
        do something
    done
while expr
    do
    done
 ```

## 计划任务
*   `at`
:   单次任务，比如`at 17:12` then `rebot`,最好Ctrl+D保存
    *   at -l
    :查询任务个数
    *   at -c index
    :   查询任务详情
    *   atrm index
    :   删除任务
*   `crontab -e`
:   进入配置周期任务编辑，分、时、日、月、星期、命令
*   `crontab -l`
:   查看任务
    *   例子   
        *   `0 0 * 5 3 /usr/sbin/reboot` 
         :   表示每年5的五月份的星期三的凌晨重启  
        *   `0 0 * 5 1，3，5 /usr/sbin/reboot` 
        :   表示每年5的五月份的星期一、三、五的凌晨重启
        *   `0 0 * 5 1-5 /usr/sbin/reboot` 
        :   表示每年5的五月份的星期一至星期五的凌晨重启
        *   `0 0 /2 * * /usr/sbin/reboot` 
        :   表示每隔2天的凌晨重启

    

     



 

    











  

