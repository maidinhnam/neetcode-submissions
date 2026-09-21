class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        lst = []
        for j in range(k):
            m = max(dct, key = dct.get)
            lst.append(m)
            del dct[m]
        return lst