class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
    
# using built-in functions

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split()[-1]
        return len(last_word)
        