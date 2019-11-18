"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/13 10:49
@File : 冒泡排序.py
@Software: PyCharm
@desc:冒泡排序
"""
def bubble_sort(arr):
    for j in range(len(arr)-1, 0, -1):
        count = 0
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
        if count == 0:
            return


arr = [7, 4, 3, 67, 34, 1, 8]
bubble_sort(arr)
print(arr)
