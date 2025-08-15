class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(goal, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
    
# dynamic programming solution - top down approach

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)              
        def can(i: int) -> bool:
            if i >= n - 1:            # at or beyond last stone
                return True
            far = min(n - 1, i + nums[i])
            for j in range(i + 1, far + 1):
                if can(j):
                    return True
            return False

        return can(0)
    
# dynamic programming solution - bottom up approach

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True                       # last index can reach itself

        for i in range(n - 2, -1, -1):      # fill from right to left
            furthest = min(n - 1, i + nums[i])
            for j in range(i + 1, furthest + 1):
                if dp[j]:
                    dp[i] = True            # i is good if any reachable j is good
                    break
        return dp[0]
