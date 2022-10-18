# -*- coding: utf-8 -*-  
""" 
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
"""

arr = [-2, 0, 10, -19, 4, 6, -8]
arr_dict = {val: idx for idx, val in enumerate(arr)}

for i in range(len(arr)):
    if arr_dict.get(2 * arr[i]) and arr_dict.get(2 * arr[i]) != i:
        print(True)