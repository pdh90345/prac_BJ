# 01타일
import sys

# sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline().strip())

dp = [0] * (n + 1)


# def tile(n: int):
#     if n == 0:
#         dp[0] = 1
#         return dp[0]
#     elif n == 1:
#         dp[1] = 1
#         return dp[1]
#     elif dp[n] != 0:
#         return dp[n]
#     else:
#         dp[n] = (tile(n - 1) + tile(n - 2)) % 15746
#         return dp[n]


# print(tile(n))


dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = (
        dp[i - 1] + dp[i - 2]
    ) % 15746  # 자료형의 정수 최대 크기를 넘어가서 오류가 난듯하다

print(dp[n])
