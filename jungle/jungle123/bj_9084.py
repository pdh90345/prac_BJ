# 동전
# 다시
import sys

t = int(input())


# for _ in range(t):
#     n = int(input())
#     coins = list(map(int, sys.stdin.readline().split()))
#     m = int(input())
#     dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
#     for i in range(n + 1):
#         dp[i][0] = 1

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if j - coins[i - 1] >= 0:
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
#             else:
#                 dp[i][j] = dp[i - 1][j]

#     print(dp[n][m])


for _ in range(t):
    n = int(input())
    coins = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    dp = [0] * (m + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, m + 1):
            dp[j] = (
                dp[j] + dp[j - coin]
            )  # 1차원 배열을 다시 초기화 하기 때문에 행이 필요없다

    print(dp[m])
