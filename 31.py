coins = [1, 2, 5, 10, 20, 50, 100, 200]
possibilities = [1] + [0 for _ in range(coins[-1])]

for coin in coins:
    for j in range(coin, coins[-1] + 1):
        possibilities[j] += possibilities[j - coin]

print("Solution:", possibilities[coins[-1]])
