class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        m = []
        for i in range(n):
            m.append(str(len(strs[i])) + '#')
            m.append(strs[i])
        return ''.join(m)
    def decode(self, s: str) -> List[str]:
        m = []
        k = 0
        while k < len(s):
            i = s.find('#', k)
            m.append(s[i+1:i+1+int(s[k:i])])
            k = i+1+int(s[k:i])
        return m

