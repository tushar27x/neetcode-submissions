class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for j in coins:
                if j <= a:
                    dp[a] = min(dp[a], dp[a-j])
            dp[a] += 1

        return dp[amount] if dp[amount] != float('inf') else -1