class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        rows = [""] * numRows
        r, step = 0, 1

        for ch in s:
            rows[r] += ch
            if r == 0:
                step = 1
            elif r == numRows - 1:
                step = -1
            r += step
        return "".join(rows)

# alternate solution - incremental counter 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res