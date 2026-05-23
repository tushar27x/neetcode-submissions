class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = float('-inf')
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(p-min_price, max_profit)

        return max_profit