# 계단오르기

import sys

n = int(input())

V = []
for _ in range(n):
    V.append(int(sys.stdin.readline().strip()))

V.insert(0, 0)


dp = [
    [0] * (n + 1) for _ in range(2)
]  # 0행 : i열까지 한칸으로 올라가는 값, 1행 : 2칸으로 올라가는 값

cnt = 0
for i in range(1, n + 1):
    if cnt == 2:
        dp[0][i] = dp[1][i - 1] + V[i]  # cnt가 2가되면 i-1열 전의 두칸으로 올라가는 값
    else:
        dp[0][i] = dp[0][i - 1] + V[i]
        cnt += 1
    if n > 1:
        dp[1][i] = max(dp[0][i - 2], dp[1][i - 2]) + V[i]

print(max(dp[0][n], dp[1][n]))
