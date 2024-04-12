# 가장 긴 증가하는 부분 수열
# 다시
import sys

n = int(input())
sequence = list(map(int, sys.stdin.readline().split()))


dp = [1] * n  # 최소 부분 수열의 길이는 1

for i in range(1, n):
    for j in range(i):  # i보다 작은 수를 확인
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[j] + 1, dp[i])

# print(dp)
print(max(dp))
