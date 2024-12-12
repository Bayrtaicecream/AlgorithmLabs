def optimal_bst(keys: list[int], freq: list[int], n: int) -> int:
    cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cost[i][i] = freq[i] 
    # 2 oos N hurtel
    for length in range(2, n + 1): 
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf') 
            total_freq = sum(freq[i:j + 1])                                                                                                             
            for r in range(i, j + 1):
                if r > i:
                    left_cost = cost[i][r - 1]
                else:
                    left_cost = 0
                if r < j:
                    right_cost = cost[r + 1][j] 
                else:
                    right_cost = 0 
                total_cost = left_cost + right_cost + total_freq
                if total_cost < cost[i][j]:                                                                                                         #hrv odo-n zrdl niit-s ih bvl shinchilchn
                    cost[i][j] = total_cost
    return cost[0][n - 1]
