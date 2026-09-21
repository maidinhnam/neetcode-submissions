class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        m = [chr(n)]
        for i in range(n):
            m.append(chr(len(strs[i])))
        for j in range(n):
            m.append(strs[j])
        return ''.join(m)
    def decode(self, s: str) -> List[str]:
        n = ord(s[0])
        m = []
        for i in range(n):
            m.append(ord(s[i+1]))
        k = n + 1
        res = []
        c = 0
        d = 0
        for j in m:
            c += j
            res.append(s[k+d:k+c])
            d += j
        return res

