class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i],0)
            count[t[i]] = count.get(t[i],0) - 1
        for val in count.values():
            if val != 0:
                return False
        return True
