#题目描述
#在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
#每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数


#思路： 从左下角开始搜索，如果target比左下角小，则向上一行，如果比它大，则向右走一列


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        num_rows = len(array) - 1
        num_cols = len(array[0]) - 1
        row = num_rows
        col = 0
        while row>=0 and col <= num_cols:
            if target < array[row][col]:
                row = row - 1
            elif target > array[row][col]:
                col = col + 1
            elif target == array[row][col]:
                return True
        if row <0 or col > num_cols:
            return False


#题目描述
#请实现一个函数，将一个字符串中的每个空格替换成“%20”。
#例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        a = s.replace(' ','%20')
        return a



#题目描述
#输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



#从头到尾遍历listNode 并append到list中，最后将list 翻转


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        list_a = []
        while listNode:
            list_a.append(listNode.val)
            listNode = listNode.next
        answer = list(reversed(list_a))
        return answer