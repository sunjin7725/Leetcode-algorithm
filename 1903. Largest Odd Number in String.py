# -*- coding: utf-8 -*-  
""" 
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number
"""

num = "52"

if int(num) % 2 == 0:
    odd_list = []
    for i in num:
        if int(i) % 2 == 1:
            odd_list.append(i)
    print(max(odd_list))
else:
    print(num)