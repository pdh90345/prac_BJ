# 구슬 찾기

import sys

n, m = map(int, sys.stdin.readline().split())
dp = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    dp[s][e] = 1


for i in range(1, n + 1):
    dp[i][i] = 0

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            dp[s][e] = min(dp[s][e], dp[s][k] + dp[k][e])

# print(dp)

hresult = [0] * (n + 1)
lresult = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j] != 0 and dp[i][j] != float("inf"):
            hresult[i] += 1
            lresult[j] += 1
count = 0
for i in range(1, n + 1):
    if hresult[i] >= (n + 1) // 2 or lresult[i] >= (n + 1) // 2:
        count += 1

print(count)
