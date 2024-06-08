# 오르막 수

import sys

input = sys.stdin.readline

n = int(input())

dp = [list(0 for _ in range(10)) for _ in range(n)]


for i in range(10):
    dp[0][i] = 1

sum = 10
for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = sum
            sum = 0
        else:
            dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]
        sum += dp[i][j]

print(sum % 10007)
