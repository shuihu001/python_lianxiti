"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2020/2/18 9:53
@File : 利用栈实现进制转换.py
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

"""二进制转十进制"""
def two_to_ten(s1):
    length = len(s1)
    s2 = s1[::-1]
    num = 0
    for i in range(length):
        num += int(s2[i])*2**i
    return num

"""十进制转其他进制"""
def ten_to_other(s1, base):
    s1 = int(s1)
    base = int(base)
    zhan = Stack()
    num = ''
    digits = '0123456789ABCDEF'
    while s1 > 0:  #入栈
        zhan.push(s1 % base)
        s1 = s1 // base
    while not zhan.isEmpty():  #出栈
        num += digits[zhan.pop()]
    return num

if __name__ == '__main__':
    i = '1'
    while i == '1':
        choose = input('二进制->十进制请输入2，十进制->其他进制请输入10：')
        if choose == "2":
            s1 = input('请输入二进制数：')
            print(two_to_ten(s1))
        else:
            base = input('想把十进制数转换成几进制呢：')
            s1 = input('好的，请输入十进制数：')
            print(ten_to_other(s1, base))
        i = input("继续请按1，结束请按任意键: ")