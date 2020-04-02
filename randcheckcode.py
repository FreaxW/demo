#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2019/6/28 12:50
# @Author     : Freax
# @File       : randcheckcode.py
# @Software   : PyCharm
# @Description:

import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import os
import uuid



class RandCheckCode:
    def __init__(self, code_length, size=(240,60), bgcolor=(0,0,0), fontsize=36):
        self._code_length = code_length
        self._size = size
        self._bgcolor = bgcolor
        self._fontpath = None
        self._fontsize = fontsize
        self._font = None
        self._image = Image.new('RGB', self._size, self._bgcolor)
        self._draw = ImageDraw.Draw(self._image)

    def set_font(self, fontpath=None, fontsize=None):
        if fontpath and fontsize:
            self._fontpath = fontpath
            self._fontsize = fontsize
            self._font = ImageFont.truetype(self._fontpath, self._fontsize)
        elif fontpath:
            self._fontpath = fontpath
            self._font = ImageFont.truetype(self._fontpath,self._fontsize)
        elif fontsize:
            self._fontsize = fontsize
            self._font = ImageFont.truetype(self._fontpath,self._fontsize)
        else:
            self._font = ImageFont.truetype(self._fontpath,self._fontsize)

    @staticmethod
    def rand_code():
        flag = random.randint(0, 1)
        if flag:  # 数字[0-9]
            return str(random.randint(0, 9))
        else:  # 字母
            return random.choice(string.ascii_letters)

    @staticmethod
    def rand_color(range_color):
        return (random.randint(range_color[0], range_color[1]),
                random.randint(range_color[0], range_color[1]),
                random.randint(range_color[0], range_color[1])
                )

    def set_image(self, size=None, bgcolor=None):
        if size and bgcolor:
            self._size = size
            self._bgcolor = bgcolor
            self._image = Image.new('RGB', self._size, self._bgcolor)
        elif size:
            self._size = size
            self._image = Image.new('RGB',self._size,self._bgcolor)
        elif bgcolor:
            self._bgcolor = bgcolor
            self._image = Image.new('RGB',self._size,self._bgcolor)
        else:
            self._image = Image.new('RGB',self._size,self._bgcolor)

    def set_draw_fill(self, range_color):
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                self._draw.point((i, j), fill=self.rand_color(range_color))

    def set_draw_text(self, offsetX, offsetY, range_color):
        for i in range(self._code_length):
            try:
                self._draw.text((offsetX + int(self._size[0] / self._code_length) * i, offsetY),
                                self.rand_code(), font=self._font, fill=self.rand_color(range_color))
            except BaseException as e:
                print(e)

    def set_iamge_BLUR(self):
        self._image = self._image.filter(ImageFilter.BLUR)

    def save_check_code(self, filedir='.'):
        try:
            os.mkdir(filedir + '/randcode')
        except FileExistsError:
            pass
        finally:
            filename = uuid.uuid4().hex + '.jpg' #生成随机字符串保存文件
            filename = os.path.join(filedir, 'randcode', filename)
            self._image.save(filename)


if __name__ == '__main__':
    code = RandCheckCode(5)
    # 设置字体格式和字体大小
    code.set_font('DejaVuSans.ttf')
    # 画随机颜色的点
    code.set_draw_fill((32,255))
    # 添加随机颜色的内容
    code.set_draw_text(15,10,(64,255))
    # 模糊滤镜 参考https://blog.csdn.net/qq_37385726/article/details/81808359
    code.set_iamge_BLUR()
    # 保存验证码文件
    code.save_check_code()




