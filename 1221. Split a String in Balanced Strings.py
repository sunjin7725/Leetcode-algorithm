"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.


Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""

s = "RLRRLLRLRL"
cnt = 0
result = 0
for i in s:
    if i == 'R': cnt += 1
    elif i == 'L': cnt -= 1

    if cnt == 0: result += 1