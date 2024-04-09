# 행렬 곱셈 순서
# 다시 해보기

import sys

n = int(input())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for diagonal in range(1, n):  # 대각선은 1부터 (0은 0으로 차있음)
    for i in range(0, n - diagonal):  # 0행부터 대각선이 존재하는 행까지
        j = i + diagonal  # 대각선에 맞는 열
        if diagonal == 1:  # 왼쪽, 아래가 0 이면 곱셈만
            dp[i][j] = (
                matrix[i][0] * matrix[i + 1][0] * matrix[j][1]
            )  # 시작행렬의 행, 마지막 행렬의 행, 마지막 행렬의 열
            continue
        dp[i][j] = sys.maxsize
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j],
                dp[i][k]
                + dp[k + 1][j]
                + matrix[i][0]
                * matrix[k + 1][0]
                * matrix[j][1],  # 시작 행렬의 행, 중간 다음 행렬의 행, 마지막 행렬의 열
            )

print(dp[0][n - 1])
