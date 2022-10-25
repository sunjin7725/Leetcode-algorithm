# -*- coding: utf-8 -*-  
""" 
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
"""

from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_cnt_dict = Counter(arr)
        result = []

        for key, value in arr_cnt_dict.items():
            if key == value:
                result.append(key)

        if any(result):
            return max(result)
        return -1