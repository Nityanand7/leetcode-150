class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
    
# dynamic programming solution - top down approach

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i: int) -> int:
            if i >= n - 1:                # already at/past last index
                return 0
            far = min(n - 1, i + nums[i]) # furthest we can try from i
            best = float('inf')
            for j in range(i + 1, far + 1):
                best = min(best, dp(j))   # min jumps from any reachable j
            return 1 + best               # take one jump to that best j

        return dp(0)
    
# dynamic programming solution - bottom up approach

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[-1] = 0                       # 0 jumps needed from last index

        for i in range(n - 2, -1, -1):
            far = min(n - 1, i + nums[i])
            best = float('inf')
            for j in range(i + 1, far + 1):
                if dp[j] < best:
                    best = dp[j]
            if best < float('inf'):
                dp[i] = 1 + best
        return dp[0]