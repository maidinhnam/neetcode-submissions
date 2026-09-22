class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        x = set(nums)
        maxi = 1
        for num in x:
            if num-1 in x:
                continue
            else:
                m = 1
                while num + 1 in x:
                    m += 1
                    num += 1
                if m > maxi:
                    maxi = m
        return maxi