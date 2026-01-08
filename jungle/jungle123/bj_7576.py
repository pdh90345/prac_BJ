# 2차원 토마토

# M=열의 개수 n은 행의 개수

import sys
from collections import deque

m, n = map(int, input().split())

d = deque()
chk = [[0] * (m) for _ in range(n)]
result = [[0] * (m) for _ in range(n)]
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            d.append((i, j))
            chk[i][j] = 1
        elif tomato[i][j] == -1:
            chk[i][j] = -1

dx = [1, 0, -1, 0]  # 하 우 상 좌
dy = [0, 1, 0, -1]

while d:
    x, y = d.popleft()
    now = tomato[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = now + 1
            chk[nx][ny] = 1
            d.append((nx, ny))

max_tomato = max(max(row) for row in tomato)
empty = any(0 in row for row in chk)
if empty:
    print(-1)
else:
    print(max_tomato - 1)
