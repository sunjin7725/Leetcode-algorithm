# -*- coding: utf-8 -*-  
""" 
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
"""
n = 10


def find_square_triple(c):
    result = 0
    for a in range(1, c):
        b = (c ** 2 - a ** 2) ** 0.5
        if int(b) == b:
            result += 1
    return result


result = 0
for i in range(1, n + 1):
    result += find_square_triple(i)
print(result)
