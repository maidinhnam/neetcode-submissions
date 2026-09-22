class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max = min(heights[l],heights[r])*r
        h1 = heights[l]
        h2 = heights[r]
        while l<r:
            while l<r and heights[l]<=heights[r]:
                l += 1
                if l<r and heights[l]>h1:
                    h1 = heights[l]
                    if max < min(heights[l],heights[r])*(r-l):
                        max = min(heights[l],heights[r])*(r-l)
                    break

            while l<r and heights[l]>heights[r]:
                r -= 1
                if l<r and heights[r]>h2:
                    h2 = heights[r]
                    if max < min(heights[l],heights[r])*(r-l):
                        max = min(heights[l],heights[r])*(r-l)
                    break
        return max