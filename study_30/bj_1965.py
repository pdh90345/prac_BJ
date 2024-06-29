# 상자 넣기

import sys

input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))

boxes.insert(0, 0)

dp = [0] * (n + 1)

for i in range(1, n + 1):
    maxValue = 0
    for j in range(i):
        if boxes[j] < boxes[i]:  # 자신보다 작은 수의 박스의 최대 개수
            maxValue = max(maxValue, dp[j])
    dp[i] = maxValue + 1  # 그 박스에 자신의 개수 1개 추가


print(max(*dp))
