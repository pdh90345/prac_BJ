# 종이의 개수

import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
check = {-1: 0, 0: 0, 1: 0}


def divide(row_s, row_e, col_s, col_e):
    new_board = set()
    for i in range(row_s, row_e + 1):
        for j in range(col_s, col_e + 1):
            new_board.add(int(board[i][j]))
            if len(new_board) > 1:
                break
        if len(new_board) > 1:
            break
    if len(new_board) == 1:
        check[new_board.pop()] += 1
    else:
        div_three = (row_e - row_s + 1) // 3
        divide(row_s, row_s + div_three - 1, col_s, col_s + div_three - 1)
        divide(
            row_s, row_s + div_three - 1, col_s + div_three, col_s + div_three * 2 - 1
        )
        divide(
            row_s,
            row_s + div_three - 1,
            col_s + div_three * 2,
            col_s + div_three * 3 - 1,
        )

        divide(
            row_s + div_three, row_s + div_three * 2 - 1, col_s, col_s + div_three - 1
        )
        divide(
            row_s + div_three,
            row_s + div_three * 2 - 1,
            col_s + div_three,
            col_s + div_three * 2 - 1,
        )
        divide(
            row_s + div_three,
            row_s + div_three * 2 - 1,
            col_s + div_three * 2,
            col_s + div_three * 3 - 1,
        )

        divide(
            row_s + div_three * 2,
            row_s + div_three * 3 - 1,
            col_s,
            col_s + div_three - 1,
        )
        divide(
            row_s + div_three * 2,
            row_s + div_three * 3 - 1,
            col_s + div_three,
            col_s + div_three * 2 - 1,
        )
        divide(
            row_s + div_three * 2,
            row_s + div_three * 3 - 1,
            col_s + div_three * 2,
            col_s + div_three * 3 - 1,
        )


divide(0, n - 1, 0, n - 1)
print(*check.values(), sep="\n")
