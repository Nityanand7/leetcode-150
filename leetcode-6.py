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