class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
    

# alternative solution using builtin startswith 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m == 0: return 0

        for i in range(len(haystack) - m + 1):
            if haystack.startswith(needle, i):
                return i
        return -1

# alternative solution using built-in find method

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)