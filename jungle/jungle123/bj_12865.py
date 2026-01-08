# 평범한 배낭
# 다시
import sys


n, k = map(int, sys.stdin.readline().split())
W = []  # 무게 리스트
V = []  # 가치 리스트
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    W.append(w)
    V.append(v)

dp = [
    [0 for _ in range(k + 1)] for _ in range(n + 1)
]  # W[i]번째 물건이 추가되었을때 j무게의 최대 가치

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j - W[i - 1] >= 0:
            dp[i][j] = max(dp[i - 1][j - W[i - 1]] + V[i - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
