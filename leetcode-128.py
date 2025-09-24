class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for i in numSet:
            if (i - 1) not in numSet:
                length = 0
                while (i + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
    
# alternate solution - using sort

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        arr = sorted(set(nums))
        longest = 1
        curr = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1
        return max(longest, curr)
