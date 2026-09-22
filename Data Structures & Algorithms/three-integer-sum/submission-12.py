class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    a = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = a
        res = []

        for c in range(0,len(nums)-2):
            l = c+1
            r = len(nums) - 1
            while l < r:
                while l<r and nums[l] + nums[r] + nums[c] < 0:
                    l += 1
                while l<r and nums[l] + nums[r] + nums[c] > 0:
                    r -= 1
                if l<r and nums[l] + nums[r] + nums[c] == 0:
                    res.append([nums[l], nums[c], nums[r]])
                l += 1

        unq = 1
        for i in range(len(res)):
            bool = False
            for j in range(unq):
                if i==j:
                    continue
                elif res[i] == res[j]:
                    bool = True
                    break
            if bool == False and i>0:
                if i>unq:
                    res[unq] = res[i]
                unq += 1
                    
        del res[unq:]
        return res  

