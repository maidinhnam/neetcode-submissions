class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unq_char = set(s)
        res = 0
        for c in unq_char:
            l = 0
            freq = 0
            for r in range(len(s)):
                if s[r] != c:
                    freq += 1
                while freq > k:
                    if s[l] != c:
                        freq -= 1
                    l += 1
                res = max(res, r-l+1)
        return res