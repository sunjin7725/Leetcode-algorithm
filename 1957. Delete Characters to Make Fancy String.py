"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
"""
from collections import deque

s = "leeetcode"
list_s = deque(s)

result = ''
before_char = ''
same_char_cnt = 1
while list_s:
    now_char = list_s.popleft()
    result += now_char
    if now_char == before_char:
        same_char_cnt += 1
    else:
        same_char_cnt = 1

    if same_char_cnt > 2:
        result = result[:-1]
        same_char_cnt -= 1

    before_char = now_char
print(result)