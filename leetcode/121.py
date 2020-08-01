class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        minp = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-minp)
            minp = min(minp, prices[i])
        
        return profit
                