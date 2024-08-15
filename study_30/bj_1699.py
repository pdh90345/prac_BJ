# 제곱수의 합

import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [sys.maxsize] * (n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    for j in range(1, i):
        square = j * j
        if square > i:  # 제곱수가 i보다 크면 break
            break
        if dp[i] > dp[i - square] + 1:  # 제곱수는 무조건 1 이므로 + 1
            dp[i] = dp[i - square] + 1


print(dp[-1])


# 시간 초과...
# n = int(input().strip())

# dp = [sys.maxsize] * (n + 1)
# dp[0] = 0
# dp[1] = 1

# for i in range(2, n + 1):
#     if i == (i // 2) ** 2:
#         dp[i] = 1
#         continue
#     for j in range(i - 1, i // 2 - 1, -1):
#         dp[i] = min(dp[i], dp[j] + dp[i - j])

# print(dp[-1])
