# 퇴사

import sys

input = sys.stdin.readline

n = int(input())
T = [0]
P = [0]
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)  # 상담 기간
    P.append(p)  # 가치

# bottom-up
dp = [0] * (n + 2)  # 기간, 가치 배열을 0 부터 만들었으므로 n+2

for i in range(1, n + 1):
    for j in range(i + T[i], len(dp)):
        if dp[j] < dp[i] + P[i]:
            dp[j] = dp[i] + P[i]

print(dp[-1])

# top-down
dp = [0] * (n + 2)  # 기간, 가치 배열을 0 부터 만들었으므로 n+2

for i in range(n, 0, -1):
    if i + T[i] < n + 2:
        dp[i] = max(dp[i + 1], dp[i + T[i]] + P[i])
    else:
        dp[i] = dp[i + 1]

print(dp[1])
