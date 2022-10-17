# -*- coding: utf-8 -*-  
""" 
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
"""
words = ["abc","car","ada","racecar","cool"]


def is_palindromic_string(text):
    if text == text[::-1]:
        return True
    return False

result = [i for i in words if is_palindromic_string(i)]
print(result)