class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_day = 0
        sell = 1
        profit = 0
        max_profit = 0

        for i in range(1, len(prices)):

            profit = prices[i] - prices[lowest_day]

            if profit < 0:
                lowest_day = i
                continue

            if profit > max_profit:
                max_profit = profit

        
        return max_profit 


        