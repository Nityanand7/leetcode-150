class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res 
            maxCount = max(maxCount, count[n])
        return res
    
# Alternate solution - Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

# You can also find lc 229 in the repo which is a variation of this problem where you need to find all elements that appear more than n/3 times. 
# It uses Misra-Gries algorithm which is a generalization of Boyer-Moore Voting Algorithm. 