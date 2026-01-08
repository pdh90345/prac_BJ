# 미로탐색


import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

d = deque()
maze = [[0 for _ in range(m)] for _ in range(n)]
walk = [[0 for _ in range(m)] for _ in range(n)]
isused = [[0 for _ in range(m)] for _ in range(n)]

maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [1, 0, -1, 0]  # 하 우 상 좌
dy = [0, 1, 0, -1]

# 거리를 deque에 넣는 방법
# d.append((0, 0, 1))
d.append((0, 0))
isused[0][0] = 1
walk[0][0] = 1
while d:
    now = d.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        # dist = now[2]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if isused[nx][ny] == 1 or maze[nx][ny] != 1:
            continue
        isused[nx][ny] = 1
        walk[nx][ny] = walk[now[0]][now[1]] + 1
        # walk[nx][ny] = dist + 1
        # d.append((nx, ny, dist + 1))
        d.append((nx, ny))

print(walk[n - 1][m - 1])
