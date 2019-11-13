"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/12 16:57
@File : 计算最大公约数.py
@Software: PyCharm
@desc:计算最大公约数
"""
def cal_max_com(x, y):
    # # 1.辗转相除法
    # temp = x % y
    # while (temp != 0):
    #     x = y
    #     y = temp
    #     temp = x % y
    # print(y)

    # # 2.辗转相减法
    # while x != y:
    #     if x > y:
    #         x -= y
    #     else:
    #         y -= x
    # print(y)

    # # 3.枚举法
    # if x > y:
    #     smaller = y
    # else:
    #     smaller = x
    # for i in range(1, smaller+1):
    #     if((x % i ==0) and (y % i ==0)):
    #         print(i)

    # 4. 欧几里得算法
    if y == 0:
        return (x)
    return (cal_max_com(y, x % y))

print(cal_max_com(13212, 26))
