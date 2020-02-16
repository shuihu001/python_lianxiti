"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2020/2/16 9:19
@File : 循环链表练习——约瑟夫环.py
@Software: PyCharm
@desc:练习循环链表
编号为1，2，...，n的n个人按顺时针方向围坐一圈，每个人有一个正整数编号。从某个位置的人开始，数
到m的人出列;下一个人（从第m+1个）又从1数起，数到m的人便是第2个出列的人；依次重复下去，直到最后一个人出列，
于是得到一个新的次序。
"""
# import numpy as np
#
#
# def Joseph(n, m):
#     # 生成初始列表
#     # a = list(np.arange(1, n+1))
#     a = [i for i in range(1, n + 1)]
#     # print(len(a))
#     p = []
#     m = m
#     while len(a) >= 1:
#         if len(a) >= m:
#             p.append(a[m-1])
#             a = a[m:].append(a[:m-1])
#
# if __name__ == '__main__':
#     Joseph(10, 3)

class Node(object):
    """结点"""
    def __init__(self,item):
        self.elem = item
        self.next = None

class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self):
        self.head = None

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            node.next = node
        else:  #判断已有一个还是多个节点
            cur = self.head
            while cur.next != self.head:  #如果有多个节点，则依次寻找
                cur = cur.next
            cur.next = node
            node.next = self.head

    def travel(self):
        cur = self.head
        while cur.next != self.head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)

    def remove(self, item):
        '''删除节点'''
        cur = self.head
        pre = None
        while cur.next != self.head:
            if cur.elem == item:
                #头节点的情况
                if cur == self.head:
                    rear = self.head
                    while rear.next != self.head:
                        rear = rear.next
                    rear.next = cur.next
                    self.head = cur.next
                else:
                    #中间结点的情况
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
    #尾节点的情况和一个元素的情况
        if cur.elem == item:
                # 一个元素的情况
            if cur == self.head:
                self.head = None
                # 尾节点元素的情况
            else:
                pre.next = self.head
                # pre.next = cur.next

    def judgement(self, m):
        cur = self.head
        count = 1
        while cur != cur.next:
            cur = cur.next
            count += 1
            if count == m:
                self.remove(cur.elem)
                print("%d-->"%cur.elem,end="")
                count = 0
        print(cur.elem)

if __name__ == '__main__':
    sll = SingleCycleLinkList()
    for i in range(1,42):
        sll.append(i)
    sll.judgement(2)
