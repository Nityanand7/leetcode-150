class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

# alternative solution using sort and comparing first and last strings

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        strs.sort()
        a, b = strs[0], strs[-1]
        i = 0
        while i < min(len(a), len(b)) and a[i] == b[i]:
            i += 1
        return a[:i]