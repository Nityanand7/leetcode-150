# using a hash set to maintain a sliding window of size k

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
    
# using a hash map to store the last seen index of each number

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in window:
                if abs(window[nums[i]] - i) <= k:
                    return True
            window[nums[i]] = i
        return False