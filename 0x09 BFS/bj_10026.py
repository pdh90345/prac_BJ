# 적록색약

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(str, input().strip())) for _ in range(n)]

r_g = [[0 for _ in range(n)] for _ in range(n)]
normal = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


d = deque()


def bfs(i, j, cnt, check):  # x, y, 각 보드별 카운트, 적록색약인지 확인
    d.append((i, j))
    if check == True:
        r_g[i][j] = cnt
    else:
        normal[i][j] = cnt
    color = board[i][j]
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if check == True:  # 적록 색약일때
                    if r_g[nx][ny] != cnt:
                        if color == "R" or color == "G":
                            if board[nx][ny] == "R" or board[nx][ny] == "G":
                                d.append((nx, ny))
                                r_g[nx][ny] = cnt
                        else:
                            if board[nx][ny] == "B":
                                d.append((nx, ny))
                                r_g[nx][ny] = cnt
                else:
                    if normal[nx][ny] != cnt:
                        if color == "R":
                            if board[nx][ny] == "R":
                                d.append((nx, ny))
                                normal[nx][ny] = cnt
                        elif color == "G":
                            if board[nx][ny] == "G":
                                d.append((nx, ny))
                                normal[nx][ny] = cnt
                        else:
                            if board[nx][ny] == "B":
                                d.append((nx, ny))
                                normal[nx][ny] = cnt


r_g_cnt = 1
nor_cnt = 1
for i in range(n):
    for j in range(n):
        if r_g[i][j] == 0:
            bfs(i, j, r_g_cnt, True)
            r_g_cnt += 1  # 마지막에 하나 더 더하므로 결과에서 -1 해준다
        if normal[i][j] == 0:
            bfs(i, j, nor_cnt, False)
            nor_cnt += 1

print(nor_cnt - 1, r_g_cnt - 1)
