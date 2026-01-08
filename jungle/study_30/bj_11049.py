# 행렬곱셈 순서

import sys

n = int(input())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]  # dp[i][j] : i번째 행렬과 j번째 행렬의 최소비용

for diagonal in range(1, n):  # 대각선
    for i in range(0, n - diagonal):
        j = i + diagonal
        if diagonal == 1:
            dp[i][j] = m[i][0] * m[i + 1][0] * m[j][1]
            continue

        dp[i][j] = float("inf")

        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j], dp[i][k] + dp[k + 1][j] + (m[i][0] * m[k + 1][0] * m[j][1])
            )

print(dp[0][n - 1])
