class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hMap:
                return [i, hMap[diff]]
            hMap[n] = i