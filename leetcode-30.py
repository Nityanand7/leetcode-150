class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        L = len(words[0])
        k = len(words)
        need = Counter(words)
        n = len(s)

        res = []
        # try each word-alignment lane
        for offset in range(L):
            left = offset
            used = 0
            window = defaultdict(int)

            # step the right pointer by word length
            for right in range(offset, n - L + 1, L):
                w = s[right:right+L]

                if w in need:
                    window[w] += 1
                    used += 1

                    # too many of word w? shrink from the left
                    while window[w] > need[w]:
                        left_w = s[left:left+L]
                        window[left_w] -= 1
                        left += L
                        used -= 1

                    # window contains exactly k words → record
                    if used == k:
                        res.append(left)

                        # slide forward by 1 word to look for overlaps
                        left_w = s[left:left+L]
                        window[left_w] -= 1
                        left += L
                        used -= 1

                else:
                    # hard reset: invalid word
                    window.clear()
                    used = 0
                    left = right + L

        return res