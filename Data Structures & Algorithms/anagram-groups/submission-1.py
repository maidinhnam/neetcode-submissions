class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for str in strs:
            l = [0]*26
            for s in str:
                l[ord(s) - ord("a")] += 1
            if tuple(l) in dct:
                dct[tuple(l)].append(str)
            else:
                dct[tuple(l)] = [str]
        return list(dct.values())


