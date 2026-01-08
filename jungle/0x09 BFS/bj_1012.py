# 유기농 배추

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
cnt = 0
d = deque()


def bfs(fx, fy):
    global cnt
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    d.append((fx, fy))
    farm[fx][fy] = 2
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if farm[nx][ny] == 1:
                    d.append((nx, ny))
                    farm[nx][ny] = 2
    cnt += 1


for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        y, x = map(int, input().split())
        farm[x][y] = 1
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                bfs(i, j)
    print(cnt)
    cnt = 0
