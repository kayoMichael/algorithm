class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = float("inf")
        for i in range(len(prices)):
            curr = min(prices[i], curr)
            profit = max(profit, prices[i] - curr)


        return profit