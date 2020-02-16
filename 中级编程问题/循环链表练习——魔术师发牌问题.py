"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2020/2/16 10:58
@File : 循环链表练习——魔术师发牌问题.py
@Software: PyCharm
@desc:练习循环链表
魔术师手中有A、2、3……J、Q、K十三张黑桃扑克牌。在表演魔术前，魔术师已经将他们按照
一定的顺序叠放好(有花色的一面朝下).魔术表演过程为:一开始,魔术师数1,
然后把最上面的那张牌翻过来,是黑桃A;然后将其放到桌面上;第二次,魔术师数1、2;
将第一张牌放到这些牌的最下面,将第二张牌翻转过来,正好是黑桃2;第三次,魔术师数1、2、3;
将第1、2张牌依次放到这些牌的最下面,将第三张牌翻过来正好是黑桃3;
……直到将所有的牌都翻出来为止.问原来牌的顺序是如何的.
"""


class Node:
    """节点"""

    def __init__(self, item):
        self.data = item
        self.next = None


class CircularLinkedList:
    """单循环链表"""

    def __init__(self):
        self.rear = None  # 尾节点

    def is_empty(self):
        return self.rear is None

    def append(self, elem):
        """尾插法"""
        temp = Node(elem)
        if self.rear is None:
            temp.next = temp
            self.rear = temp
        else:
            temp.next = self.rear.next
            self.rear.next = temp
            self.rear = temp

    def print_all(self):
        """
        按顺序打印全部节点
        """
        if self.is_empty():
            return
        p = self.rear.next  # 取得头部节点
        print('Head', end='')
        while True:
            print('-->', p.data, end='')
            if p is self.rear:  # 到达尾部停止
                break
            p = p.next
        print('-->Finish')


def solution_circular_linked_list():
    pokers = CircularLinkedList()
    for _ in range(13):
        pokers.append(0)

    temp = pokers.rear
    for num in range(1, 14):
        i = 0
        while i < num:
            temp = temp.next
            if temp.data == 0:
                i += 1
        temp.data = num

    print('#' * 50)
    print('\n牌组: ')
    pokers.print_all()
    print('\n' + '#' * 50)

if __name__ == '__main__':
    solution_circular_linked_list()