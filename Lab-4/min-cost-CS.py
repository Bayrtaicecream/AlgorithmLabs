class Solution: 
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)                                                                                                                                                                     
        if n == 0:                                                                                               
            return 0                                                                                                                                                                                   
        elif n == 1: 
            return cost[0]                                                                                                                                                     
        dp = [0] * n                                                                                                                                               
        dp[0] = cost[0]  #ehni shtig
        dp[1] = cost[1]  #2doh shtig
        for i in range(2, n): #2 --> N
                                                                                                                                                                                                   
            #dp[i-1] dp[i-2]
            if dp[i - 1] > dp[i - 2]:                                                                                                                                                                    
                dp[i] = dp[i - 2] + cost[i]                                                                                                                                                           
            else: 
                dp[i] = dp[i - 1] + cost[i]
        if dp[n - 2] > dp[n - 1]:  
            return dp[n - 1]                                                                                                                                                                     
        else:
            return dp[n - 2]  

