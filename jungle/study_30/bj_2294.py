# 동전 2

import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coin = int(sys.stdin.readline().strip())
    coins.append(coin)

dp = [sys.maxsize] * (k + 1)
dp[0] = 0


for coin in coins:
    for i in range(k + 1):
        if i >= coin:
            dp[i] = min(dp[i - coin] + 1, dp[i])


if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
