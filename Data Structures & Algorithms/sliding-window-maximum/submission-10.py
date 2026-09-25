class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        res = []
        q.append(0)
        head = 0
        if k == 1:
            return nums
        for i in range(1,len(nums)):
            if i-q[head] >= k:
                head += 1
            while nums[i]> nums[q[-1]] and len(q)-1>= head:
                q.pop()
                if len(q) == head:
                    break
            q.append(i)
            if i >= k-1:
                res.append(nums[q[head]])

        return res
