    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        mini, ans = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] > mini:
                ans = max(ans, prices[i] - mini)
            else:
                mini = prices[i]
        return ans