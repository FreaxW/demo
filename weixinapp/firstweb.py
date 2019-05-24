#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author:freax
Date:2019/5/24 15:53
DESC:
微信公众号开发demo
1、https://mp.weixin.qq.com 申请一个公众号。
2、->基本配置。
    2.1、使用flask轻量级web框架搭建一个网站,获得一个URL。
    2.2、填写URL，->提交,然后获取微信的GET请求参数里echostr的值并原样返回。
3、用户发消息给公号，微信服务器把消息封装成xml数据包，然后给URL发送POST请求，URL响应该POST请求。
    3.1 解析xml数据包,获取参数。
    3.2 根据参数类别，返回对应内容。
"""

from flask import Flask, request
from xml.etree import ElementTree as ET
from flask import render_template

app = Flask(__name__)

# 访问方式：ip:port/ 如192.168.1.2:5000/
@app.route('/', methods=['GET,''POST','OPTIONS','PUT','DELETE','HEAD','CONNECT','TRACE'])  # default GET，如果不设置则无法接受POST请求
def index():
    # 处理配置url时，微信服务器发来的确认消息 GET
    if request.method == 'GET':
        echostr = request.args.get('echostr')
        return echostr
    # 处理用户发送的消息 POST
    elif request.method == 'POST':
        data = request.get_data()  # xml
        xml = ET.fromstring(data)
        '''
        新建一个index.html文件，用过滤器替换里面内容
        <xml>
              <ToUserName><![CDATA[{{to_username}}]]></ToUserName>
              <FromUserName><![CDATA[{{from_username}}]]></FromUserName>
              <CreateTime>{{create_time}}</CreateTime>
              <MsgType><![CDATA[{{text}}]</MsgType>
              <Content><![CDATA[{{content}}]]></Content>
        </xml>
    '''
        ToUserName = xml.findtext('.//ToUserName')
        FromUserName = xml.findtext('.//FromUserName')
        CreateTime = xml.findtext('.//CreateTime')
        MsgType = xml.findtext('.//MsgType')
        Content = xml.findtext('.//Content')

        # 针对不同类型，返回不同的内容
        if MsgType == 'text':
            # 定义不同文本内容，返回的内容
            if Content == '1':
                return render_template(
                    './index.html',
                    to_username=FromUserName,
                    from_username=ToUserName,
                    create_time=CreateTime,
                    text=MsgType,
                    context='')
            # 返回你好！
            else:
                return render_template(
                    './index.html',
                    to_username=FromUserName,
                    from_username=ToUserName,
                    create_time=CreateTime,
                    text=MsgType,
                    context='你好！')
    # 其他请求方式 OPTIONS,PUT,DELETE,HEAD,CONNECT,TRACE
    else:
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
