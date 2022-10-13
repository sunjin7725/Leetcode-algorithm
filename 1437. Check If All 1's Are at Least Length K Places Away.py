"""
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

nums = [1,0,0,0,1,0,0,1], k = 2
"""
from typing import List

nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        length = 0
        find_one = False
        for num in nums:
            if not find_one and num == 1:
                find_one = True
            elif find_one and num == 1:
                if k > length:
                    return False
            if find_one and num == 0:
                length += 1
        return True