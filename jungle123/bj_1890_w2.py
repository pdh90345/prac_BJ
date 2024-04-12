# 점프

import sys
from collections import deque

n = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


cnt = 0
d = deque()

dx = [1, 0]  # 하 우
dy = [0, 1]

d.append((0, 0))
while d:
    x, y = d.popleft()
    w = board[x][y]
    for i in range(2):
        nx = x + w * dx[i]
        ny = y + w * dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if nx == n - 1 and ny == n - 1:
                cnt += 1
            elif board[nx][ny] == 0:
                continue

            else:
                d.append((nx, ny))

print(cnt)
