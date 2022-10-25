# -*- coding: utf-8 -*-  
""" 
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
"""
s = "1"

continuous_zero = 0
continuous_one = 0
max_zero = 0
max_one = 0

before_num = ''
for num in s:
    if before_num == num:
        if num == '1': continuous_one += 1
        elif num == '0': continuous_zero += 1
    else:
        if num == '1':
            max_zero = max(continuous_zero, max_zero)
            continuous_one = 1
        elif num == '0':
            max_one = max(continuous_one, max_one)
            continuous_zero = 1
    before_num = num
max_zero = max(continuous_zero, max_zero)
max_one = max(continuous_one, max_one)
print(max_zero, max_one)