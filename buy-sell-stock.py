class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10**4 + 1
        sell = 0
        
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > sell:
                sell = prices[i] - buy
        return sell