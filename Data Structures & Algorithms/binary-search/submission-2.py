class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if target < nums[l] or target > nums[r]:
            return -1
        elif target == nums[l]:
            return l
        elif target == nums[r]:
            return r
        while r > l+1:
            if nums[(r+l)//2] < target:
                l = (r+l)//2
            elif nums[(r+l)//2] > target: 
                r = (r+l)//2
            else:
                return (r+l)//2
        return -1