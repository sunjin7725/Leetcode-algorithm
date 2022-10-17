# -*- coding: utf-8 -*-  
"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Input: s = "abcde", goal = "cdeab"
Output: true
"""
s = "abcde"
goal = "cdeab"


def text_shift(text):
    return text[-1] + text[:-1]


for _ in range(len(s)):
    s = text_shift(s)
    print(s)
    if s == goal:
        print(True)
        break

