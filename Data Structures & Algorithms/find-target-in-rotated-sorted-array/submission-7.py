class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        res = -1
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        while r>l+1:
            n = (r+l)//2
            if nums[n] == target:
                res = n
                break
            elif ((nums[n]>nums[n+1]) or (nums[n]<nums[n-1])) and (target < nums[r]):
                l = n
            elif ((nums[n]>nums[n+1]) or (nums[n]<nums[n-1])) and (target > nums[r]):
                r = n
            elif (nums[n] > nums[r] and target>nums[r] and target < nums[n]) or (nums[n] < nums[r] and target<nums[r] and target < nums[n]):
                r = n
            else:
                l = n
        return res