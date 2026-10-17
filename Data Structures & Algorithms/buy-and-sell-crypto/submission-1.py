class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        buy_price = prices[0]
        for sell_price in prices:
            if sell_price <= buy_price:
                buy_price = sell_price
            else:
                curr_profit = sell_price - buy_price
                max_profit = max(max_profit, curr_profit)
        
        return max_profit
