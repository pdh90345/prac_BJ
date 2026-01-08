# 미로 만들기

import sys, heapq
from collections import deque

n = int(input())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
# d = deque()
pq = []

chkRoom = [[sys.maxsize for _ in range(n)] for _ in range(n)]
# chkRoom = [[-1 for _ in range(n)] for _ in range(n)]

dx = [1, 0, -1, 0]  # 하 우 상 좌
dy = [0, 1, 0, -1]

heapq.heappush(pq, (0, 0, 0))
chkRoom[0][0] = 0
while pq:
    d, x, y = heapq.heappop(pq)
    if x == n - 1 and y == n - 1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if chkRoom[nx][ny] != sys.maxsize:
            continue
        if maze[nx][ny] == 1:
            chkRoom[nx][ny] = min(chkRoom[nx][ny], d)
        else:
            chkRoom[nx][ny] = min(chkRoom[nx][ny], d + 1)
        heapq.heappush(pq, (chkRoom[nx][ny], nx, ny))

print(chkRoom[n - 1][n - 1])


# d.append((0, 0))
# chkRoom[0][0] = 0
# while d:
#     x, y = d.popleft()
#     if x == n - 1 and y == n - 1:
#         break
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#             continue
#         if chkRoom[nx][ny] != -1:  # 처음 온게 아니라면 -> 이미 흰 방으로 방문했단 뜻
#             continue
#         if maze[nx][ny] == 1:
#             chkRoom[nx][ny] = chkRoom[x][y]
#             d.appendleft((nx, ny))
#         else:
#             chkRoom[nx][ny] = chkRoom[x][y] + 1
#             d.append((nx, ny))

# print(chkRoom[n - 1][n - 1])
