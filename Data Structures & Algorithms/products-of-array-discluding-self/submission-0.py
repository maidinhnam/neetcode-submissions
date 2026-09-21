class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]*len(nums)
        r = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                l[i] = 1
            else:
                l[i] = l[i-1]*nums[i-1]
        for j in range(len(nums)-1,-1,-1):
            if j == len(nums)-1:
                r[j] = 1
            else:
                r[j] = r[j+1]*nums[j+1]
        res = [1]*len(nums)
        for k in range(len(nums)):
            res[k] = l[k] * r[k]
        return res
