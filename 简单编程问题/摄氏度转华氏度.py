"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/11 14:49
@File : 摄氏度转华氏度.py
@Software: PyCharm
@desc:摄氏度转华氏度
"""
def c_to_h():
    c = input("请输入摄氏度温度： ")
    c = float(c)
    print(str(32 + 1.8*c)+("h"))
c_to_h()