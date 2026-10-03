class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            price_if_i_sell_today = current_price - min_price
            max_profit = max(max_profit, price_if_i_sell_today)
            min_price = min(current_price, min_price)
        return max_profit


        