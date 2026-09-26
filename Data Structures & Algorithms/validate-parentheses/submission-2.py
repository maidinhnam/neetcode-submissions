class Solution:
    def isValid(self, s: str) -> bool:
        b = True
        dct1 = {'(':0, '[':1, '{':2}
        dct2 = {')':0, ']':1, '}':2}
        l = []
        if len(s)%2 == 1:
            b = False
        for i in range(len(s)):
            if s[i] in dct1:
                l.append(s[i])
            elif s[i] in dct2: 
                if len(l)>0 and dct2[s[i]] == dct1[l[-1]]:
                    l.pop()
                else:
                    b = False
            else:
                b = False
        if l != []:
            b = False
        return b