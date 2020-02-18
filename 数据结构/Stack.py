"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2020/2/18 10:58
@File : Stack.py
@Software: PyCharm
@desc:
"""
"""定义栈"""
class Stack(object):
    #初始化栈
    def __init__(self):
        self.items = []

    #判断是否为空
    def isEmpty(self):
        return self.items == []

    #栈尾添加新元素
    def push(self, item):
        self.items.append(item)

    #栈尾删除元素
    def pop(self):
        return self.items.pop()

    #查看栈的大小
    def size(self):
        return len(self.items)