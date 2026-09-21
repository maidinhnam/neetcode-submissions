class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        freq = [[] for _ in range(len(nums))]
        for j in dct:
            freq[dct[j]-1].append(j)
        lst = []
        for n in range(len(freq) -1, -1, -1):
            if freq[n] != [] and len(lst) < k:
                for num in freq[n]:
                    lst.append(num)
            elif len(lst) == k:
                break
        return lst