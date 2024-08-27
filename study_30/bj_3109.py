# 빵집

import sys, copy

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]
chkBoard = [[0 for _ in range(c)] for _ in range(r)]


def upRight(x, y):
    if board[x - 1][y + 1] == "." and chkBoard[x - 1][y + 1] == 0:
        return True
    return False


def downRight(x, y):
    if board[x + 1][y + 1] == "." and chkBoard[x + 1][y + 1] == 0:
        return True
    return False


def dfs(x, y):
    if y == c - 1:  # 마지막 열에 도달
        return 1
    else:
        if x - 1 >= 0 and upRight(x, y):  # 오위로 갈 수 있다면
            chkBoard[x - 1][y + 1] = 1
            if dfs(x - 1, y + 1) == 1:
                return 1
            chkBoard[x - 1][y + 1] = 0
        if board[x][y + 1] == "." and chkBoard[x][y + 1] == 0:  # 오른쪽
            chkBoard[x][y + 1] = 1
            if dfs(x, y + 1) == 1:
                return 1
            chkBoard[x][y + 1] = 0
        if x + 1 < r and downRight(x, y):  # 오아래
            chkBoard[x + 1][y + 1] = 1
            if dfs(x + 1, y + 1) == 1:
                return 1
            chkBoard[x + 1][y + 1] = 0

        if (
            (x - 1 < 0 and board[x][y + 1] == "X" and board[x + 1][y + 1] == "X")
            or (
                board[x - 1][y] == "X"
                and board[x][y + 1] == "X"
                and board[x + 1][y + 1] == "X"
            )
            or (x + 1 >= r and board[x - 1][y] == "X" and board[x][y + 1] == "X")
        ):
            board[x][y] = "X"


ans = 0
for i in range(r):
    if dfs(i, 0) == 1:
        ans += 1
print(ans)
