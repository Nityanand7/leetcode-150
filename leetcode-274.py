# optimized solution - counting sort

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0] * (n + 1)

        for c in citations:
            paper_counts[min(c, n)] += 1
        
        h = n
        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[h]
        
        return h

# descending sort

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h
    
# ascending sort

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i, c in enumerate(citations):
            h = n - i
            if c >= h:
                return h
        return 0
    
# Try every possible h (from n down to 0)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for h in range(n, -1, -1):
            cnt = 0
            for c in citations:
                if c >= h:
                    cnt += 1
            if cnt >= h:
                return h
        return 0
    
# Grow h one step at a time

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        h = 0
        while h < n:
            cnt = 0
            for c in citations:
                if c >= h + 1:
                    cnt  += 1
            if cnt >= h+1:
                h += 1
            else:
                break
        return h
