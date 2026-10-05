class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1+dfs(amount - coin))
            
            dp[amount] = res
            return res
        
        no_of_coins = dfs(amount)
        return -1 if no_of_coins >= 1e9 else no_of_coins 
            
        
