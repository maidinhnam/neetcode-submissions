class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)
            
            if total_hours <= h:
                ans = mid         
                right = mid - 1
            else:
                left = mid + 1    
                
        return ans