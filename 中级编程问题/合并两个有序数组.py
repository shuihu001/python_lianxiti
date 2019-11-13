"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2019/11/12 17:33
@File : 合并两个有序数组.py
@Software: PyCharm
@desc:合并两个有序数组
"""
def merge_sort(nums1, nums2):
    m = []
    i, j = 0, 0
    while nums1 and nums2:
        if nums1[i] <= nums2[j]:
            temp = nums1.pop(i)
            m.append(temp)
        else:
            temp = nums2.pop(j)
            m.append(temp)

    m = m + nums1 + nums2
    return m

nums1 = [1,2,3,4]
nums2 = [2,3,4,5,6]
a = merge_sort(nums1, nums2)
print(a)