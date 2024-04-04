# 경쟁적 전염

import sys, heapq

n, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

pq = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

s = 0

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            heapq.heappush(pq, (s, board[i][j], i, j))

while pq:
    s, w, x, y = heapq.heappop(pq)
    if s == S:  # 시간이 넘어가면 확인하지 않는다
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = w
                heapq.heappush(pq, (s + 1, board[nx][ny], nx, ny))


print(board[X - 1][Y - 1])
