from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        memo[0] = 0 
        
        return self.coinChangeHelper(coins, amount, memo)

    def coinChangeHelper(self, coins: List[int], amount: int, memo: List[int]) -> int:
        if amount < 0:
            return -1
        
        if memo[amount] != -1:
            return memo[amount]

        minCoins = float("inf")
        
        for coin in coins:
            res = self.coinChangeHelper(coins, amount - coin, memo)
            if res >= 0:  
                minCoins = min(minCoins, res + 1)
        
        memo[amount] = -1 if minCoins == float("inf") else minCoins
        return memo[amount]
