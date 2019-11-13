"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/11 15:47
@File : 反转字符串.py
@Software: PyCharm
@desc:反转字符串
"""
from functools import reduce
def reverse():
    w = input("请输入一个字符串： ")
    #  1.切片
    print(w[::-1])

    #  2.列表的reverse
    # w = list(w)
    # w.reverse()
    # print("".join(w))

    #  3.使用reduce
    # print(reduce(lambda x,y:y+x,w))

    # #  4.递归
    # def func(w):
    #     if len(w) < 1:
    #         print(w)
    #     print(func(w[1:]) + w[0])
    # func(w)

    # #  5.使用栈
    # w = list(w)
    # result = ""
    # while len(w) > 0:
    #     result += w.pop()
    # print(result)

    #  6.for循环
    # result = ""
    # max_index = len(w)-1
    # for index, word in enumerate(w):
    #     result += w[max_index - index]
    # print(result)

if __name__ == '__main__':
    reverse()