class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1
            
            for i in range(min(count, 2)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
    
# alternate solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 2

        if len(nums) <= 2:
            return len(nums)

        for r in range(2, len(nums)):
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1
        
        return l
