"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/11 15:26
@File : 判断素数.py
@Software: PyCharm
@desc:判断素数
"""
import math
def judge_prime():
    num = int(input("输入你想判断的数： "))
    if num == 1:
        print(num, "不是素数")
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if (num % i) == 0:
                print(num, "不是素数")
                break
        else:
            print(num, "是素数")

judge_prime()