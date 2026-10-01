class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = min(nums[l], nums[r])
        while r > l+1:
            n = (r+l)//2
            if nums[n] > max(nums[l], nums[r]):
                l = n
            elif nums[n] < max(nums[l], nums[r]):
                r = n
                res = min(res, nums[n])
        return res