# 쉬운 계단 수

import sys

n = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(10)] for _ in range(n + 1)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

ans = sum(dp[n]) % 1000000000
print(ans)
