# -*- coding: utf-8 -*-  
""" 
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
"""
import re
from collections import Counter

password = "IloveLe3tcode!"


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if self.length_check(password) and self.has_lowercase(password) and \
           self.has_uppercase(password) and self.has_digit(password) and \
           self.has_special_character(password) and self.check_same_char(password):
            return True
        return False

    def length_check(self, pwd):
        if len(pwd) >= 8: return True
        return False

    def has_lowercase(self, pwd):
        if len(re.sub('[^a-z]', '', pwd)) > 0: return True
        return False

    def has_uppercase(self, pwd):
        if len(re.sub('[^A-Z]', '', pwd)) > 0: return True
        return False

    def has_digit(self, pwd):
        if len(re.sub('[^0-9]', '', pwd)) > 0: return True
        return False

    def has_special_character(self, pwd):
        if len(re.sub(r'[^!@#$%^&*()-+]', '', pwd)) > 0: return True
        return False

    def check_same_char(self, pwd):
        before_char = ''
        for char in pwd:
            if char == before_char: return False
            before_char = char
        return True

test = "-Aa1a1a1"
