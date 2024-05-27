# 불

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs_f():  # 불
    while d_f:
        x, y = d_f.popleft()
        cur = building[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if building[nx][ny] == "#":
                    continue
                elif building[nx][ny] == ".":
                    d_f.append((nx, ny))
                    building[nx][ny] = cur + 1


def bfs_s():  # 상근
    global possible, result
    while d_s:
        x, y = d_s.popleft()
        cur = building[x][y]
        if x == 0 or x == h - 1 or y == 0 or y == w - 1:  # 빌딩의 끝까지 도착하면 탈출
            possible = True
            result = cur + 1  # type: ignore
            return
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if building[nx][ny] == "#":
                    continue
                if building[nx][ny] == ".":
                    d_s.append((nx, ny))
                    building[nx][ny] = cur + 1
                elif (
                    building[nx][ny] > cur + 1
                ):  # 불과 동시에 접근하는 상황 막기위해 cur + 1
                    d_s.append((nx, ny))
                    building[nx][ny] = cur + 1


for _ in range(t):
    w, h = map(int, input().split())  # 열, 행
    building = [list(map(str, input().strip())) for _ in range(h)]
    d_f = deque()
    d_s = deque()
    possible = False
    result = 0
    for i in range(h):
        for j in range(w):
            if building[i][j] == "*":
                d_f.append((i, j))
                building[i][j] = 0  # type: ignore # 해당 칸의 수 : 몇초 뒤에 도착하는지
            if building[i][j] == "@":
                d_s.append((i, j))
                building[i][j] = 0  # type: ignore
    bfs_f()  # 불부터 빌딩을 채우고
    bfs_s()  # 시간 초가 작으면 덮어 씌우는 형식
    if possible:
        print(result)
    else:
        print("IMPOSSIBLE")
