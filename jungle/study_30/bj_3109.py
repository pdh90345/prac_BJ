# 빵집

import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(r)]
chkBoard = [[0 for _ in range(c)] for _ in range(r)]


# 시간 2000ms
def dfs(x, y):
    chkBoard[x][y] = 1  # 현재 위치를 방문 처리
    if y == c - 1:  # 마지막 열에 도달했다면
        return True

    # 오른쪽 위, 오른쪽, 오른쪽 아래 순서로 탐색
    for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
        nx, ny = x + dx, y + dy
        if (
            0 <= nx < r
            and 0 <= ny < c
            and board[nx][ny] == "."
            and chkBoard[nx][ny] == 0
        ):
            if dfs(nx, ny):
                return True

    return False


ans = 0
for i in range(r):
    if dfs(i, 0):
        ans += 1

print(ans)

# 시간 3000ms
# 함수 오버헤드와 복잡한 조건문으로 인하여 1000ms 정도 차이가 난다.

# def upRight(x, y):
#     if board[x - 1][y + 1] == "." and chkBoard[x - 1][y + 1] == 0:
#         return True
#     return False


# def downRight(x, y):
#     if board[x + 1][y + 1] == "." and chkBoard[x + 1][y + 1] == 0:
#         return True
#     return False


# def dfs(x, y):
#     if y == c - 1:  # 마지막 열에 도달
#         return 1
#     else:
#         if x - 1 >= 0 and upRight(x, y):  # 오위로 갈 수 있다면
#             chkBoard[x - 1][y + 1] = 1
#             if dfs(x - 1, y + 1) == 1:
#                 return 1
#         if board[x][y + 1] == "." and chkBoard[x][y + 1] == 0:  # 오른쪽
#             chkBoard[x][y + 1] = 1
#             if dfs(x, y + 1) == 1:
#                 return 1
#         if x + 1 < r and downRight(x, y):  # 오아래
#             chkBoard[x + 1][y + 1] = 1
#             if dfs(x + 1, y + 1) == 1:
#                 return 1

# ans = 0
# for i in range(r):
#     if dfs(i, 0) == 1:
#         ans += 1
# print(ans)
