"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        move_indexer = 0
        for idx, num in enumerate(nums):
            if num % 2 == 0:
                tmp = nums[move_indexer]
                nums[move_indexer] = num
                nums[idx] = tmp
                move_indexer += 1
        return nums


nums = [3, 1, 2, 4]
print(Solution().sortArrayByParity(nums))
