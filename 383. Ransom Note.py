# -*- coding: utf-8 -*-  
""" 
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false
"""
ransomNote = "aa"
magazine = "aab"

print(set(ransomNote) - set(magazine))