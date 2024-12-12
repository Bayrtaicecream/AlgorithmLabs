import unittest


def fractional_knapsack(weights, profits, n, backpack_capacity):

    max_profit = 0
    current_weight = 0
    items = []

    for i in range(len(weights)):
        items.append((profits[i] / weights[i], profits[i], weights[i]))

    items.sort(key=lambda x: x[0], reverse=True)


    for _, profit, weight in items:
        if current_weight + weight <= backpack_capacity:
            max_profit += profit
            current_weight += weight
        else:
            remaining_capacity = backpack_capacity - current_weight
            max_profit += profit * (remaining_capacity / weight)
            break

    return max_profit

class TestFractionalKnapsack(unittest.TestCase):
    def test_basic_case(self):
        weights = [10, 20, 30]
        profits = [60, 100, 120]
        backpack_capacity = 50
        expected_profit = 240.0  
        self.assertAlmostEqual(fractional_knapsack(weights, profits, len(weights), backpack_capacity), expected_profit)
if __name__ == '__main__':
    unittest.main()
