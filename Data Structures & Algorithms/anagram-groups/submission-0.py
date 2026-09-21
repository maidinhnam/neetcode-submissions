class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = {}
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) in lst:
                lst[''.join(sorted(strs[i]))].append(strs[i])
            else:
                lst[''.join(sorted(strs[i]))] = [strs[i]]
        result = []
        for j in lst.values():
            result.append(j)
        return result
