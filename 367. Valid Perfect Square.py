# -*- coding: utf-8 -*-  
""" 
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Input: num = 16
Output: true
"""
num = 16

sqrt_num = num ** 0.5
if int(sqrt_num) == sqrt_num:
    print(True)