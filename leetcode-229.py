class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        threshold = len(nums) // 3
        res = []
        for n, c in freq.items():
            if c > threshold:
                res.append(n)
        return res


# Alternate solution - Using Counter from collections

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [n for n, c in freq.items() if c > len(nums) // 3]


# Alternate solution - Misra-Gries Algorithm for n/3 majority elements - O(1) space complexity

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = defaultdict(int)

        for n in nums:
            candidates[n] += 1

            if len(candidates) <= 2:
                continue
            new_cand = defaultdict(int)
            for n, c in candidates.items():
                if c > 1:
                    new_cand[n] = c - 1
            candidates = new_cand 

        res = []
        for n in candidates:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res 
        
