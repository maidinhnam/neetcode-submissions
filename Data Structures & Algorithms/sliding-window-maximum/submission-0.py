class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []  
        head = 0  
        res = []

        for i in range(len(nums)):
            
            if head < len(q) and q[head] < i - k + 1:
                head += 1

            
            while head < len(q) and nums[q[-1]] <= nums[i]:
                q.pop()

            
            q.append(i)

            
            if i >= k - 1:
                res.append(nums[q[head]])

        return res