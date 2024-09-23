from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Number of transactions allowed
        max_transactions = 2
        
        # Initialize the dp array
        dp = [[0] * len(prices) for _ in range(max_transactions + 1)]
        
        for t in range(1, max_transactions + 1):
            max_profit = -prices[0]  # Maximum profit before day 0
            for d in range(1, len(prices)):
                # Update the maximum profit for this transaction
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_profit)
                # Update max_profit to include the profit from previous day
                max_profit = max(max_profit, dp[t - 1][d] - prices[d])
        
        return dp[max_transactions][-1]

