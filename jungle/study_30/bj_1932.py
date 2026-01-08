# 정수 삼각형

import sys

input = sys.stdin.readline

n = int(input())

tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

result = 0

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = tri[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tri[i][0]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + tri[i][i]
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + tri[i][j], dp[i - 1][j] + tri[i][j])
if n == 1:
    print(tri[0][0])
else:
    print(max(*dp[n - 1]))
