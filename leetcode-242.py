class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        if len(s) != len(t):
            return False
            
        for char in s:
            if char in mapS:
                mapS[char] += 1
            else:
                mapS[char] = 1

        for char in t:
            if char not in mapS:
                return False
            elif mapS[char] == 1:
                del mapS[char]
            else:
                mapS[char] -= 1
        
        return True