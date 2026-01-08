# 피리부는 사나이 다시 풀어보기

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]

chkBoard = [list(0 for _ in range(m)) for _ in range(n)]
cnt = 0

dir = ["D", "R", "U", "L"]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(i, j):
    global cnt
    d = deque()
    d.append((i, j))
    while d:
        x, y = d.popleft()
        if chkBoard[x][y] == 1:
            if (x, y) in cycle:
                cnt += 1
        else:
            chkBoard[x][y] = 1
            cycle.append((x, y))
            k = dir.index(board[x][y])
            nx = x + dx[k]
            ny = y + dy[k]
            d.append((nx, ny))


for i in range(n):  # 행
    for j in range(m):  # 열
        if chkBoard[i][j] == 0:
            cycle = []
            dfs(i, j)
print(cnt)
