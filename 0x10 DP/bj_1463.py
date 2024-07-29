# 1로 만들기

import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [-1] * (n + 1)
dp[1] = 0

for i in range(1, n + 1):
    if dp[i] == -1:
        result = sys.maxsize
        if i % 3 == 0:
            result = min(result, dp[i // 3] + 1)
        if i % 2 == 0:
            result = min(result, dp[i // 2] + 1)
        result = min(result, dp[i - 1] + 1)
        dp[i] = result

print(dp[-1])
