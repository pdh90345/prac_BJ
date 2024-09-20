# 피리부는 사나이

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]

chkBoard = [list(-1 for _ in range(m)) for _ in range(n)]
cnt = 0


def dfs(x, y):
    global cnt
    d = deque()
    d.append((x, y))
    while d:
        dx, dy = d.popleft()
        if chkBoard[dx][dy] == cnt:
            return True
        elif -1 < chkBoard[dx][dy] < cnt:
            return False
        else:
            chkBoard[dx][dy] = cnt
            if board[dx][dy] == "D":
                if dx + 1 >= n:
                    return True
                else:
                    if -1 < chkBoard[dx + 1][dy] < cnt:
                        chkBoard[dx][dy] = chkBoard[dx + 1][dy]
                    d.append((dx + 1, dy))
            elif board[dx][dy] == "U":
                if dx - 1 < 0:
                    return True
                else:
                    if -1 < chkBoard[dx - 1][dy] < cnt:
                        chkBoard[dx][dy] = chkBoard[dx - 1][dy]
                    d.append((dx - 1, dy))
            elif board[dx][dy] == "R":
                if dy + 1 >= m:
                    return True
                else:
                    if -1 < chkBoard[dx][dy + 1] < cnt:
                        chkBoard[dx][dy] = chkBoard[dx][dy + 1]
                    d.append((dx, dy + 1))
            else:
                if dy - 1 < 0:
                    return True
                else:
                    if -1 < chkBoard[dx][dy - 1] < cnt:
                        chkBoard[dx][dy] = chkBoard[dx][dy - 1]
                    d.append((dx, dy - 1))


for i in range(n):  # 행
    for j in range(m):  # 열
        if chkBoard[i][j] == -1:
            if dfs(i, j):
                cnt += 1
print(cnt)
