# 바닥장식

import sys
from collections import deque


n, m = map(int, input().split())  # 행 개수 , 열 개수

floor = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

result = n * m

for i in range(n):
    for j in range(m):
        if j < m - 1 and floor[i][j] == "-":  # 열의 끝이 아니고 '-' 일때
            if floor[i][j + 1] == "-":
                result -= 1
        elif i < n - 1 and floor[i][j] == "|":  # 행의 끝이 아니고 '|' 일때
            if floor[i + 1][j] == "|":
                result -= 1

print(result)
