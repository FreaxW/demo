## 安装 PCRE
> PCRE 作用是让 Nginx 支持 Rewrite 功能
-   下载并解压
`wget https://sourceforge.net/projects/pcre/files/pcre/8.44/pcre-8.44.tar.gz`
`tar zxvf pcre-8.44.tar.gz`

-   安装
    -   切换目录`cd pcre-8.44`
    -   检查环境`./configure`
    -   编译安装 `make && make install`
-   查看版本（检查是否安装成功）
`pcre-config --version`

## 安装 Nginx
-   下载并解压
`wget http://nginx.org/download/nginx-1.17.9.tar.gz`
`tar zxvf nginx-1.17.9.tar.gz`

- 目录介绍
    -   查找目录 `locate nginx-1.17.9` or `find / -name nginx-1.17.9` or `which nginx` or`whereis`
    -   切换目录 `cd nginx-1.17.9` 
    -   目录结构
        -   auto
            >   库、os、编译器cc,用于系统有哪些库供nginx使用，以及操作系统的特性。
        -   change
            >   本次更新的内容
        -   conf
            >   示例文件
        -   contrib
            >   vim目录表示nginx.conf的高亮语法文件,将其目录下所有文件拷贝到etc/vim/vimrc/配即可使用`cp -r contrib/vim/* /etc/vim/`
        -   html
            >   两个html文件，一个50x错误，一个nginx的 首页欢迎界面
        -   man
            >   linux对nginx的帮助文件
        -   src
            >   源文件                                    
-   编译安装
    -   编译前检查配置 `./configure --prefix=/usr/local/webserver/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-44`
        -   --prefix指定路径
        -   --with表示要编译默认不编译的模块，--without相反，所有的要编译的模块都在objs/ngx_modules.c文件中
    -   编译安装 `make && make install`
        >   编译时生成的中间文件在objs中，很重要很重要很重要！！！热部署（升级而不重启）的时候需要替换它
-   添加环境变量
    -   打开`vim /etc/profile`添加 `PATH=$PATH:/usr/local/webserver/nginx/sbin`
    -   重新加载profile文件 `source /etc/profile`
-   查看版本（检查是否安装成功）
`/usr/local/webserver/nginx/sbin/nginx -v` or `nginx -v`
-   启动nginx
`/usr/local/webserver/nginx/sbin/nginx`
-   查看nginx
`ps-ef|grep nginx`
`ps -A|grep nginx`
-   nginx 命令
    >   可使用nginx --help获取命令帮助
    -   -g 
        >   覆盖.conf中的指令
    -   -p
        >   指定运行命令，会替换掉.conf中设置的目录
    -   -c
        >   以指定的.conf文件启动
    -   -s
        >   通过发送信号去操作运行中的nginx
        -   重载配置文件  reload
        -   立刻停止    stop
        -   优雅的退出   quit
        -   重新开始记录文件    reopen
    -   -t
        >   检查.conf是否存在语法错误

## 配置Nginx
    >nginx的配置文件在nginx.conf中

-   默认`cat nginx.conf`
    ```
        #user  nobody;
        worker_processes  1;
        
        #error_log  logs/error.log;
        #error_log  logs/error.log  notice;
        #error_log  logs/error.log  info;
        
        #pid        logs/nginx.pid;
        
        
        events {
            worker_connections  1024;
        }
        
        
        http {
            include       mime.types;
            default_type  application/octet-stream;
        
            #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
            #                  '$status $body_bytes_sent "$http_referer" '
            #                  '"$http_user_agent" "$http_x_forwarded_for"';
        
            #access_log  logs/access.log  main;
        
            sendfile        on;
            #tcp_nopush     on;
        
            #keepalive_timeout  0;
            keepalive_timeout  65;
        
            #gzip  on;
        
            server {
                listen       80;
                server_name  localhost;
        
                #charset koi8-r;
        
                #access_log  logs/host.access.log  main;
        
                location / {
                    root   html;
                    index  index.html index.htm;
                }
        
                #error_page  404              /404.html;
        
                # redirect server error pages to the static page /50x.html
                #
                error_page   500 502 503 504  /50x.html;
                location = /50x.html {
                    root   html;
                }
        
                # proxy the PHP scripts to Apache listening on 127.0.0.1:80
                #
                #location ~ \.php$ {
                #    proxy_pass   http://127.0.0.1;
                #}
        
                # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
                #
                #location ~ \.php$ {
                #    root           html;
                #    fastcgi_pass   127.0.0.1:9000;
                #    fastcgi_index  index.php;
                #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
                #    include        fastcgi_params;
                #}
        
                # deny access to .htaccess files, if Apache's document root
                # concurs with nginx's one
                #
                #location ~ /\.ht {
                #    deny  all;
                #}
            }
        
        
            # another virtual host using mix of IP-, name-, and port-based configuration
            #
            #server {
            #    listen       8000;
            #    listen       somename:8080;
            #    server_name  somename  alias  another.alias;
        
            #    location / {
            #        root   html;
            #        index  index.html index.htm;
            #    }
            #}
        
        
            # HTTPS server
            #
            #server {
            #    listen       443 ssl;
            #    server_name  localhost;
        
            #    ssl_certificate      cert.pem;
            #    ssl_certificate_key  cert.key;
        
            #    ssl_session_cache    shared:SSL:1m;
            #    ssl_session_timeout  5m;
        
            #    ssl_ciphers  HIGH:!aNULL:!MD5;
            #    ssl_prefer_server_ciphers  on;
        
            #    location / {
            #        root   html;
            #        index  index.html index.htm;
            #    }
            #}
        }
    ```
-   nginx.conf介绍
    -   user 组名 用户名;
        -   创建用户组和用户
            >   `/usr/sbin/groupadd admin`
            >   `/usr/sbin/useradd -g admin admin`        
    -   worker_processes cpu核数; 
        >   工作进程数，`ps -elf | grep nginx` 可以找到nginx的worker进程ID,通过`cat /proc/{id}/limits`查看内存占用情况
    -   4个服务
        -   http
        -   upstream
        -   server
        -   location
           
           
## 热部署
-   备份二进制文件`cp nginx nginx.old`
-   将最新编译的二进制文件nginx复制到sbin目录下替换原来的nginx中
`cp -r nginx /usr/local/webserver/nginx/sbin -f`
-   向mster进程发送一个信号让其新启一个master进程(改进程是通过最新的二进制文件启动的，然后开始过度)`kill USR2 master进程id`
-   发送一个信号让老的master进制优雅的关闭(有一个master进程还会存在，为了版本回退)`kill WATCH masterid`

## 使用Nginx搭建一个静态页面
-   准备一个静态文件夹statics
-   配置一个location
    ```
        location / { # 表示所有的请求都会来到下面指定的目录
            alias statics/;
            autoindex on;当用户访问/statics目录时展示目录下所有的文件
            set $limit_rate 1k;设置nginx向浏览器的响应的速度,表示每秒/1k
    }
    ```
-   开启gzip压缩静态文件
    ```
        gzip on;
        gzip_min_length 1; #表示小于1k的不压缩
        gzip_types html css js; # 针对文件类型压缩
    ```
-   开启gzip压缩静态文件
-   设置日志格式
    ```
        log_format main '$remote_addr -$remote_user [$time_local]"$request" '  #设置名字为main的日志格式
        '$stitus $body bytes sent "Shttp referer" '
        '"$http_user_agent" "$http_x_forwarded_for"';
        access_log logs/access.log main; # 设置日志文件
    ```