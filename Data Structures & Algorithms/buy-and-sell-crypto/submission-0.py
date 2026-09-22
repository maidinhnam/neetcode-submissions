class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minl = prices[0]
        res = 0
        for i in range(len(prices)):
            if prices[i] < minl:
                minl = prices[i]
            else:
                res = max(res, prices[i] - minl)
        return res