# 빙산
# 다시 풀기
import sys
from collections import deque

r, c = map(int, input().split())

ice = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = deque()

count = 0
year = 1
melt_ice = set()


def bfs(x, y, year):
    global r, c
    d.append((x, y))
    visited[x][y] = year
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                break
            if visited[nx][ny] < year and ice[nx][ny] == 0:
                if ice[x][y] > 0:
                    ice[x][y] -= 1
            if visited[nx][ny] < year and ice[nx][ny] > 0:
                d.append((nx, ny))
                visited[nx][ny] = year
        melt_ice.add(ice[x][y])


count_chk = True  # 빙산이 하나다


while True:
    count = 0
    for i in range(r):
        for j in range(c):
            if visited[i][j] < year and ice[i][j] != 0:
                bfs(i, j, year)
                count += 1
            if count == 2:
                count_chk = False
                break
    if len(melt_ice) == 1:
        count_chk = True
        break
    elif count_chk == False:
        break
    else:
        year += 1


if count_chk == False:
    print(year - 1)
else:
    print(0)
