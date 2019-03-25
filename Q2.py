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






