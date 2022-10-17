# -*- coding: utf-8 -*-  
""" 
There is a hidden integer array arr that consists of n non-negative integers.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved that the answer exists and is unique.

Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
"""

def nor(a, b):
    result = ''
    for i in bin((a | b)):
        if i == 0:
            result += '1'
        else:
            result += '0'
    return int(result)

first = 1
encoded = [1,2,3]

result = [first]
for i in encoded:
    result.append(result[-1] ^ i)
print(result)


00
10

10