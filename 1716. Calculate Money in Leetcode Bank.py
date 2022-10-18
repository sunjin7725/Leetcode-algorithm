# -*- coding: utf-8 -*-  
""" 
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
"""


def summation(_from, _to):
    return int((_from + _to) * (_to - _from + 1) / 2)

n = 20
result = 0

for i in range((n//7) + 1):
    if i == (n//7):
        result += summation(1 + i, (n % 7) + i)
    else:
        result += summation(1 + i, 7 + i)
print(result)