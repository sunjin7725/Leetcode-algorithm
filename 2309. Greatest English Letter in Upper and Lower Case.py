# -*- coding: utf-8 -*-  
""" 
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.
"""


def find_lower_with_upper(text):
    pass


def isupper(char):
    if 65 <= ord(char) <= 90:
        return True
    return False


s = "cNujweccyqgoPGNWrwjXXjtyQYyGgQQNPCjZZrgCPWggrPjutsEoIoEqgwjqcYtYsWGsjEegsqNXNQtWcYywcuCyQysuqZYgqIZYrrsGNuPgPsusuIqcIXcgEyWPugWgqQoeXyjygWcNCqGXYuGWPGCQqrjCQNNtPeIoQCEreGEgqyrYcNYCZqjtYYXIItXtrtQWPerCtgwcPYuqINywcrWjttZoEqQGyPgoCtrGGoyIsWCrYYscIQqwEyseIgGjEZquNusyWNGuNoEQEQoZWtQPuyojGyyguZYXcsejoNZIWZYWyYsZNGwtGNXuYjCtPEGtgsuCeoYuqEIcXZIgrZXstEEPCyugCqNCwgZZWCcGXrrtgCNjGwtyjWgsGXrgEouuyrEwseoXCtuygsZQENoyscCqyWZyGQEwZCNCQXoeuGIysqGrsweXctQNXIowNPtYwrQEsgeWoyNejXEGjwGQIoscqoPgtGjXuqPGCXQroQECjtgqEeyQEINYNuWgqIucwYCqruoEQcyqoQyoNurowYruYYZeXXrwyCPjWsY"

s = sorted(set(s))
result_list = []
for char in s:
    if isupper(char):
        if char.lower() in s:
            result_list.append(char)
    else: break
print(result_list)