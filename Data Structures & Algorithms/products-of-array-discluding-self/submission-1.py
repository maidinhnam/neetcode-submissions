class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        p = 1
        for i in range(1,len(nums)):
            p = p*nums[i-1]
            res[i] = p
        q = 1
        for j in range(len(nums)-2,-1,-1):
            q = q*nums[j+1]
            res[j] = q*res[j]   
        return res
