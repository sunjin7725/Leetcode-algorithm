# -*- coding: utf-8 -*-  
""" 
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
"""
arr = [1, 2, 2, 1, 1, 3]
unique_arr = list(set(arr))
occurrences_arr = [arr.count(i) for i in unique_arr]

if len(occurrences_arr) == len(set(occurrences_arr)):
    print(True)