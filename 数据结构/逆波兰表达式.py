"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2020/2/18 10:58
@File : 逆波兰表达式.py
@Software: PyCharm
@desc:
"""
from Stack import Stack

# 判断符号优先级
def priority(z):
    if z in ['x', 'y', 'z']:
        return 2
    elif z in ['+', '-']:
        return 1

# 中缀表达式准换成后缀表达式
"""
(1) 初始化两个栈：运算符栈S1和储存中间结果的栈S2；
(2) 从左至右扫描中缀表达式；
(3) 遇到操作数时，将其压入S2；
(4) 遇到运算符时，比较其与S1栈顶运算符的优先级：
(4-1) 如果S1为空，或栈顶运算符为左括号“(”，则直接将此运算符入栈；
(4-2) 否则，若优先级比栈顶运算符的高，也将运算符压入S1（注意转换为前缀表达式时是优先级较高或相同，而这里则不包括相同的情况）；
(4-3) 否则，将S1栈顶的运算符弹出并压入到S2中，再次转到(4-1)与S1中新的栈顶运算符相比较；
(5) 遇到括号时：
(5-1) 如果是左括号“(”，则直接压入S1；
(5-2) 如果是右括号“)”，则依次弹出S1栈顶的运算符，并压入S2，直到遇到左括号为止，此时将这一对括号丢弃；
(6) 重复步骤(2)至(5)，直到表达式的最右边；
(7) 将S1中剩余的运算符依次弹出并压入S2；
(8) 依次弹出S2中的元素并输出，结果的逆序即为中缀表达式对应的后缀表达式（转换为前缀表达式时不用逆序）。
"""
def zhon_to_hou(expr):
    stack = []
    post = []
    for z in expr:
        if z not in ['x', '*', '/', '+', '-', '(', ')']:  # 字符直接输出
            post.append(z)
            # print(1, post)
        else:
            if z != ')' and (not stack or z == '(' or stack[-1] == '('
            or priority(z) > priority(stack[-1])):  # stack 不空；栈顶为（；优先级大于
                stack.append(z) # 运算符入栈
            elif z == ')':  # 右括号出栈
                while True:
                    x = stack.pop()
                    if x != "(":
                        post.append(x)
                        # print(2, post)
                    else:
                        break
            else:  # 比较运算符优先级，看是否入栈出栈
                while True:
                    if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
                        post.append(stack.pop())
                        # print(3, post)
                    else:
                        stack.append(z)
                        break
    while stack:  # 还未出栈的运算符，需要加到表达式末尾
        post.append(stack.pop())
    return post


if __name__ == '__main__':
    stack = Stack()
    # RPN_str = '1 2 + 3 4 - *'
    # RPN_str = input('请输入一个逆波兰表达式，用空格隔开：')
    str = input('请输入一个算数表达式：')
    RPN_str = zhon_to_hou(str)
    RPN_str = ' '.join(RPN_str)
    print(RPN_str)
    for c in RPN_str.split():
      if c in '+-*':
        i2 = stack.pop()
        i1 = stack.pop()
        print(i1,c,i2)
        print(eval('%s'*3 % (i1,c,i2)))
        stack.push(eval('%s'*3 % (i1,c,i2)))
      else:
        stack.push(c)
    print('result', stack.pop())