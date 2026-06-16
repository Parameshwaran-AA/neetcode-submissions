class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        Min_price = prices[0]
        profit = 0
        Max_price = 0

        for i in range(len(prices)):

            Min_price = min(prices[i], Min_price)
            
            profit = prices[i] - Min_price

            Max_price = max(profit, Max_price)

    
        return Max_price
        