class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        if s == '':
            return 0
        maxi = 1
        l = 0
        for r in range(len(s)):
            if s[r] not in last_index:
                last_index[s[r]] = r
            elif s[r] in last_index and last_index[s[r]]>=l:
                l = last_index[s[r]] + 1
                last_index[s[r]] = r
            else:
                last_index[s[r]] = r
            maxi = max(maxi, r-l+1)

        return maxi