# 42. Trapping Rain Water - Space Complexity O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        maxLeft = [0] * n 
        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])

        maxRight = [0] * n
        maxRight[n - 1] = height[n - 1]
        for i in range(n - 2, -1,-1):
            maxRight[i] = max(maxRight[i + 1], height[i])

        water = 0
        for i in range(n):
            water += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        
        return water
    
