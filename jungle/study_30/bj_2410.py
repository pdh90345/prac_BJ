# 2의 멱수의 합
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

dp[1] = 1

for i in range(2, n + 1):
    if i % 2 == 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i // 2]

print(dp[n] % 1000000000)

# dp = [1] * (n + 1) # 동전 식

# i = 2
# while i <= n:
#     for j in range(n + 1):
#         if j >= i:
#             dp[j] = dp[j] + dp[j - i]
#     i = i * 2

# print(dp[n] % 1000000000)
