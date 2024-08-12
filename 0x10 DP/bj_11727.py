# 2*n 타일링2

import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [0] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
        continue
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = dp[i - 1] + (dp[i - 2] * 2)

print(dp[-1] % 10007)
