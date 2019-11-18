"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/13 10:56
@File : 快排序.py
@Software: PyCharm
@desc:快排序：1.选择基准值 2.根据大于和小于基准值把元素分成两个子数组 3.分别对子数组进行快排序
        时间复杂度O(nlog n )
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
a=[10,5,2,3]
print(quicksort(a))