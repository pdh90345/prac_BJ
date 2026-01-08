# 3차원 토마토

import sys
from collections import deque

m, n, h = map(int, input().split())

tomato = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)
]

d = deque()
chk = [[[0] * m for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                d.append((i, j, k))
                chk[i][j][k] = 1
            elif tomato[i][j][k] == -1:
                chk[i][j][k] = -1

dz = [1, 0, 0, -1, 0, 0]  # 전 하 우 후 상 좌
dx = [0, 1, 0, 0, -1, 0]
dy = [0, 0, 1, 0, 0, -1]

while d:
    z, x, y = d.popleft()
    now = tomato[z][x][y]
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if tomato[nz][nx][ny] == 0:
            tomato[nz][nx][ny] = now + 1
            chk[nz][nx][ny] = 1
            d.append((nz, nx, ny))
max_tomato = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            max_tomato = max(max_tomato, tomato[i][j][k])
            if chk[i][j][k] == 0:
                max_tomato = -1
                break
        if max_tomato == -1:
            break
    if max_tomato == -1:
        break

if max_tomato == -1:
    print(max_tomato)
else:
    print(max_tomato - 1)
