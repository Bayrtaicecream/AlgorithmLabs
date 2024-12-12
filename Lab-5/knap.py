# def knapsack(W, weights, values, n):
#     dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]                                                                                                                                      #2d matrx uusgn
#             #[0][0][0]                                                                                                                                       #n+1 mur, W+1 bgna umnh shg bugd adil 0-r duurcihsn bga 
#             #[0][0][0]                                                                                                                                            # mur ed zuils, bgna uurgvchd bgth jingn hmje.
#             #[0][0][0]
#     for i in range(1, n + 1):
#         for j in range(W + 1):
#             if weights[i - 1] <= j:                                                                                                                 #hrv odo-n ed zuils-n jin uurgvch-n odo-n daatsas bga bvl

#                #dp[i - 1][j - weights[i - 1]] + values[i - 1].                                                                                                                      hmgin ih buyu untei-g avna
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])                                                                                     #dhj yum hih blmjtoi gsn ug
#             else:
#                 dp[i][j] = dp[i - 1][j]                                                                                                                     #hih blmjq blhr ym higeq-r grsn hmgin untei ni

    
#     return dp[n][W]

# W = 50
# weights = [10, 20, 30]
# values = [60, 100, 120]
# n = len(weights)
# print(knapsack(W, weights, values, n))


import unittest

def knapsack(W, weights, values, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][W]

class TestKnapsack(unittest.TestCase):
    
    def test_knapsack(self):
        #  case 1
        W = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(weights)
        self.assertEqual(knapsack(W, weights, values, n), 220)
    

if __name__ == '__main__':
    unittest.main()

