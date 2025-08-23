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
    
# 42. Trapping Rain Water - Space Complexity O(1) - 2 pointers

class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res