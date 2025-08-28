class Solution:
    def reverseWords(self, s: str) -> str:
        string_builder = collections.deque()
        n = len(s)
        i = 0

        while i < n:
            
            while i < n and s[i] == " ":
                i += 1

            if i == n:
                break
            
            start = i
            while i < n and s[i] != " ":
                i += 1
            string_builder.appendleft(s[start:i])
        return " ".join(string_builder)
    
# alternate solution - using split and join

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])