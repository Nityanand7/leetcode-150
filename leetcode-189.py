class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return 
        
        k %= n

        res = [0] * n 

        for i, v in enumerate(nums):
            res[(i+k) % n] = v 
        
        nums[:] = res

# solution with O(1) space complexity
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        k %= n

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            
        reverse(0, n - 1)   #all elements
        reverse(0, k - 1)   #first k elements
        reverse(k, n - 1)   #last n - k elemets