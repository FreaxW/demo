# h1
## h2
### h3
#### h4
##### h5
###### h6

这是一级标题
===
这是二级标题
---

<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=#0099ff size=12 face="黑体">黑体</font>
<font color=#00ffff size=3>null</font>
<font color=gray size=5>gray</font>

> 这段文字将被高亮显示...

[点击跳转至百度](http://www.baidu.com)
![图片](https://upload-images.jianshu.io/upload_images/703764-605e3cc2ecb664f6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
* 黄瓜
* 玉米
* 茄子

+ 黄瓜
+ 玉米
+ 茄子

- 黄瓜
- 玉米
- 茄子

1. 黄瓜
2. 玉米
3. 茄子

    <table>     
      <tr>
        <td>Foo</td>
      </tr>
    </table>  

*   段落一

    小段一
*   段落二

    小段二
    
* 段落一
    > 区块标记一
* 段落二
    > 区块标记二
    
***
---

*这里是斜体*
_这里是斜体_

**这里是加粗**
__这里是加粗__

```
fun (x: Int, y: Int): Int {
  return x + y
}
```


表头|条目一|条目二
:---:|:---:|:---:
项目|项目一|项目二

\   反斜线
`   反引号
*   星号
_   底线
{}  花括号
[]  方括号
()  括弧
#   井字号
+   加号
-   减号
.   英文句点
!   惊叹号

#如何给文字上色
单纯使用Markdown设置文字颜色已经做不到:

    先用Markdown编辑完成
    导出为html，在需要上色的部分手动添加标签<font color='#ff0000'></font>保存即可。
    工具Pandoc
    参考 Installing 安装 Pandoc。
    pandoc -o hello.html hello.md
#引用
> 欢迎关注“freax”的博客  
> 始于颜值、陷于才华、忠于人品

> 这是一级引用
>> 这是二级引用
>>> 这是三级引用  
>   return shell_exec("echo $input | $markdown_script");
- [x] 已完成项目1
  - [x] 已完成事项
  - [ ] 代办事项
- [ ] 代办项目2
- [ ] 代办项目3

        :--- 代表左对齐
        :--: 代表居中对齐
        ---: 代表右对齐
        ---- 默认左对齐

dog | bird | cat
----|------|----
foo | foo  | foo
bar | bar  | bar
baz | baz  | baz

```
graph TD

    A[Christmas] -->B(Go Shopping)
    B --> C{Let me think}
    C -->|one| D[Laptop]
    C -->|two| E[iPhone]
    C -->|three| F[Car]
```

gantt
    dateFormat YYYY-MM-DD
    title 产品计划表
    section 初期阶段
    明确需求: 2016-03-01, 10d
    section 中期阶段
    跟进开发: 2016-03-11, 15d
    section 后期阶段
    走查测试: 2016-03-20, 9d
    
`print("hello world")`

Markdown
:   轻量级文本标记语言，可以转换成html，pdf等格式（左侧有一个可见的冒号和四个不可见的空格）  
代码块 2
:   这是代码块的定义（左侧有一个可见的冒号和四个不可见的空格） 
        代码块（左侧有八个不可见的空格）

<ol>
    <li>Bird</li>
    <li>McHale</li>
    <li>Parish</li>
</ol>

I get 10 times more traffic from [Google] [1] than from [Yahoo] [2] or [MSN] [3].

  [Google](http://google.com/)        "Google"  
  [Yahoo](http://search.yahoo.com/)  "Yahoo Search"  
  [MSN](http://search.msn.com/)    "MSN Search"
  
[Google](http://google.com/)



* * *
***
*****
- - -
---------------------------------------
<hr color="red" size="10" />

~~这是一条删除线~~

这是一个注脚测试[^footer1]

[^footer1]
:   这是一个测试，用来阐释注脚。

在HEXO中显示没用，其他的上面又有用，我也不清楚啦

#流程图
flow
    st=>start: Start:>https://www.zybuluo.com
    io=>inputoutput: verification
    op=>operation: Your Operation
    cond=>condition: Yes or No?
    sub=>subroutine: Your Subroutine
    e=>end
    st->io->op->cond
    cond(yes)->e
    cond(no)->sub->io
    
###自动链接
<http://example.com/>


\*literal asterisks\*


###表情 
<https://github.com/guodongxiaren/README/blob/master/emoji.md>  
:scream:
:airplane:
:laughing: 
:ok:
:airplane: 
##数学公式

$$E=mc^2$$

##不想使用markdown support+Paste Images into Markdown的组合，也可以使用Markdown Navigator插件
