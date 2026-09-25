class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dct = {}
        dcs = {}
        n = 0
        l = 0
        f = len(s)
        res = ""
        b1 = False
        b2 = False
        for i in range(len(t)):
            dcs[t[i]] = 0
            if t[i] in dct:
                dct[t[i]] += 1
            else:
                dct[t[i]] = 1
        for r in range(len(s)):
            if s[r] in dcs:
                
                if b1 == False:
                    l = r
                    b1 = True
                dcs[s[r]] += 1
                if dcs[s[r]] == dct[s[r]]:
                    n += 1
                    if b2 == False and n == len(dct):
                        res = s[l:r+1]
                        b2 ==True

            if s[r] in dcs and n==len(dct):
                while n >= len(dct) :

                    if s[l] in dct:

                        if dcs[s[l]] -1 < dct[s[l]]:
                            if r-l+1 < f:
                                f = min(f,r-l+1)
                                res = s[l:r+1]

                            break
                        else:

                            dcs[s[l]] -= 1
                    
                    l += 1
        return res
