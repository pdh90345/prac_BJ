# 전쟁 - 전투

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())  # y(열 개수), x(행 개수)

board = [list(map(str, input().strip())) for _ in range(m)]
check = [[0 for _ in range(n)] for _ in range(m)]

dx = [1, 0, -1, 0]  # 하 우 상 좌
dy = [0, 1, 0, -1]


def bfs(boardColor, i, j):
    d = deque()
    d.append((i, j))
    check[i][j] = 1
    cnt = 1
    while d:
        x, y = d.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if check[nx][ny] == 0 and board[nx][ny] == boardColor:
                    cnt += 1
                    d.append((nx, ny))
                    check[nx][ny] = 1
    return cnt


wTeam = 0
bTeam = 0
for i in range(m):
    for j in range(n):
        if check[i][j] == 0:
            power = bfs(board[i][j], i, j)
            if board[i][j] == "W":
                wTeam += power * power
            else:
                bTeam += power * power

print(wTeam, bTeam)
