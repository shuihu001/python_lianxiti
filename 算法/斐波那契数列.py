"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/13 10:59
@File : 斐波那契数列.py
@Software: PyCharm
@desc:
"""
# 1.递归 写法最简洁，但是效率最低，会出现大量的重复计算，时间复杂度O（1.618^n）,而且最深度1000
# def Fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
#
#
# for i in range(1, 20):
#     print(Fibonacci(i), end=' ')

# 2.递推法 递推法，就是递增法，时间复杂度是 O(n)，呈线性增长，如果数据量巨大，速度会越拖越慢
# def fib_loop(n):
#     a, b  = 0, 1
#     for i in range(n+1):
#         a, b = b, a+b
#     return a
#
#
# for i in range(20):
#     print(fib_loop(i), end=" ")


# 3.生成器 带有yield的函数都被看成生成器，生成器是可迭代对象
# def fib_loop(n):
#     a, b  = 0, 1
#     for i in range(n+1):
#         a, b = b, a+b
#         yield a
# for i in fib_loop(10):
#     print(i, end=' ')

#  4.使用矩阵
### 1
import numpy


# def fib_matrix(n):
#     res = pow((numpy.matrix([[1, 1], [1, 0]])), n) * numpy.matrix([[1], [0]])
#     return res[0][0]
# for i in range(10):
#     print(int(fib_matrix(i)), end=' ')
# #
# ### 2
# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = numpy.matrix("1 1;1 0")
    # 返回是matrix类型
    return pow(Matrix, n)  # pow函数速度快于 使用双星好 **

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(numpy.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list
# 调用
f = Fibonacci_Matrix(10)
print(f)