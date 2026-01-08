# 단지번호 붙이기

import sys
from collections import deque

n = int(input())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]  # 지도
check = [[0 for _ in range(n)] for _ in range(n)]  # 방문 확인


dx = [1, 0, -1, 0]  # 하 우 상 좌
dy = [0, 1, 0, -1]
d = deque()

result = []  # 단지 저장 배열


def bfs(x: int, y: int):
    d.append((x, y))
    check[x][y] = 1
    now = 1  # 현재 집 개수
    while d:
        cx, cy = d.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1 and check[nx][ny] == 0:
                d.append((nx, ny))
                now += 1
                check[nx][ny] = now
    result.append(now)


for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and check[i][j] == 0:
            bfs(i, j)

print(len(result))
result.sort()
for item in result:
    print(item)
