# -*- coding: utf-8 -*-  
"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: rowIndex = 3
Output: [1,3,3,1]
"""
from functools import reduce
rowIndex = 3
pascal_triangle = [[1]]

for idx in range(rowIndex):
    pascal_triangle.append([1] +
                           [pascal_triangle[idx][i] + pascal_triangle[idx][i + 1] for i in range(len(pascal_triangle[idx]) - 1)] +
                           [1])
print(pascal_triangle)