# O(1) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

# O(mn) space

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(mn) space
        m, n = len(matrix), len(matrix[0])
        copy = [row[:] for row in matrix]

        for r in range(m):
            for c in range(n):
                if copy[r][c] == 0:
                    for cc in range(n):
                        matrix [r][cc] = 0
                    for rr in range(m):
                        matrix [rr][c] = 0

# O(m + n) space

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(m+n) space
        m, n = len(matrix), len(matrix[0])
        zero_rows = [False] * m
        zero_cols = [False] * n

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows[r] = True
                    zero_cols[c] = True
        
        for r in range(m):
            for c in range(n):
                if zero_rows[r] or zero_cols[c]:
                    matrix[r][c] = 0