class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        x = set(nums)
        l = list(x)
        lst = []
        for i in range(len(x)):
            if l[i]-1 in x:
                continue
            else:
                lst.append(l[i])
        max = 1
        for j in range(len(lst)):
            m = 1
            while lst[j] + 1 in x:
                m += 1
                lst[j] =  lst[j] + 1
            if m > max:
                max = m
        return max