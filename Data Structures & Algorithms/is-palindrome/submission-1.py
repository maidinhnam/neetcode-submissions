class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = s.lower()

        r = []

        for char in l:
            if ('a' <= char <= 'z') or ('0' <= char <= '9'):
                r.append(char)

        for i in range(len(r)//2):
            if r[i] != r[len(r)-i -1]:
                return False
        return True
