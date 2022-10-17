# -*- coding: utf-8 -*-  
""" 
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
"""

pattern = "abba"
s = "dog cat cat dog"

word_dict = {}
pattern_dict = {}
word_pattern = ''

for idx, word in enumerate(s.split()):
    if word_dict.get(word, None):
        word_pattern += word_dict.get(word)
    else:
        if not pattern_dict.get(pattern[idx], None):
            word_dict[word] = pattern[idx]
            pattern_dict[pattern[idx]] = word
            word_pattern += pattern[idx]
        else:
            pass


print(word_pattern)