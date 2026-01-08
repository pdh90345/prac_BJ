# 첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다.
# 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다.
# 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

import sys

n = int(input())  # 변의 길이
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 색종이


def checkBoard(board: list):
    return all(element == board[0][0] for row in board for element in row)  # 같은색?


bc = 0  # 파란색
wc = 0  # 하얀색


def div(board: list, rf: int, rl: int, cf: int, cl: int):
    global bc, wc
    midr = (rf + rl) // 2
    midc = (cf + cl) // 2
    # part_board = [row[cf:cl+1] for row in board[rf:rl+1]]
    part_board = []
    for i in range(rf, rl + 1):
        row = board[i]
        part_row = row[cf : cl + 1]
        part_board.append(part_row)
    if checkBoard(part_board):
        if part_board[0][0] == 1:
            bc += 1
        else:
            wc += 1
    else:
        div(board, rf, midr, cf, midc)
        div(board, rf, midr, midc + 1, cl)
        div(board, midr + 1, rl, cf, midc)
        div(board, midr + 1, rl, midc + 1, cl)


div(board, 0, n - 1, 0, n - 1)
print(wc)
print(bc)
