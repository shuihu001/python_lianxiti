"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/13 10:50
@File : 选择排序.py
@Software: PyCharm
@desc:选择排序：每次找一个最小的，时间复杂度O(n²)
"""


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
a = [4,6,2,3,8,1]
# print(findSmallest(a))


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
print(selection_sort(a))