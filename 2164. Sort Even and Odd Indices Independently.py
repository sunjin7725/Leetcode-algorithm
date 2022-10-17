# -*- coding: utf-8 -*-  
""" 
You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

Sort the values at odd indices of nums in non-increasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
Sort the values at even indices of nums in non-decreasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
Return the array formed after rearranging the values of nums.

Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation:
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].
"""
nums = [5, 39, 33, 5, 12, 27, 20, 45, 14, 25, 32, 33, 30, 30, 9, 14, 44, 15, 21]
even_indices = []
odd_indices = []
for i in range(len(nums)):
    if i % 2 == 0:
        even_indices.append(nums[i])
    else:
        odd_indices.append(nums[i])

even_indices = sorted(even_indices)
odd_indices = sorted(odd_indices, reverse=True)

result = []
for i in range(len(odd_indices)):
    result.append(even_indices[i])
    result.append(odd_indices[i])

if len(nums) % 2 == 1:
    result.append(even_indices[-1])
