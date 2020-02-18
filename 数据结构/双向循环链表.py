"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2020/2/16 12:10
@File : 双向循环链表.py
@Software: PyCharm
@desc:
"""


class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubelCircularLinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def length(self):
        if self.is_empty():
            return 0
        else:
            cur = self.head
            num = 0
            while cur.next != self.head:
                cur = cur.next
                num += 1
            return num+1

    def ergotic(self):
        if self.is_empty():
            raise ValueError("ERROR NULL")
        else:
            cur = self.head.next
            print(self.head.item)
            while cur != self.head:
                print(cur.item)
                cur = cur.next

    def add(self, item):  #头部增加节点
        node = Node(item)
        if self.is_empty():
            node.next = node
            node.prev = node
            self.head = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head = node

    def append(self, item):
        node = None(item)
        if self.is_empty():
            self.add(item)
        else:
            self.head.prev.next = node
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev = node

    def insert(self, index, item):
        if index == 0:
            self.add(item)
        elif index > self.length() - 1:
            self.append(item)
        else:
            cur = self.head
            num = 1
            while cur.next != self.head:
                if num == index:
                    break
                cur = cur.next
                num += 1
            node = Node(item)
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node


    def delet(self, index):
        if self.is_empty():
            raise ValueError("ERROR NULL")
        elif index == 0 and self.length()==1:
            self.head = None
        elif index == 0 and self.length() > 1:
            self.head.prev.next = self.head.next
            self.heaf.next.prev = self.head.prev
            self.head = self.head.next
        elif index == self.length()-1:
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head
        else:
            cur = self.head
            num = 1
            while cur.next != self.head:
                if num == index:
                    break
                cur = cur.next
                num += 1
            cur.next.next.prev = cur
            cur.next = cur.next.next

   