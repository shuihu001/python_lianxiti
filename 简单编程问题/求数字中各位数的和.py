"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/11 14:53
@File : 求数字中各位数的和.py
@Software: PyCharm
@desc:求数字中各位数的和
"""
import math


#首先判断它是几位数
def JiWei(num):
    a = num
    c =0
    while a != 0:
        a = int(a/10)
        c += 1
    return c


# 取最高位，求和
def sum_all(num):
    c = JiWei(num)
    if num < 10:
        return num
    else:
        H = int(num / math.pow(10, c-1)) #最高位
        y = int(num - H * math.pow(10, c-1))  #取高位后剩余

        n = H + sum_all(y)
        return n


def main():
    num = int(input("请输入一个正整数 "))
    sum = sum_all(num)
    print(sum)

if __name__ == '__main__':
    main()