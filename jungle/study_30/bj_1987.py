# 알파벳
# 다시 풀기

import sys

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(map(str, input().strip())) for _ in range(r)]


check = set()

dx = [1, 0, -1, 0]  # 하 우 상 좌
dy = [0, 1, 0, -1]

result = 0
memo = {}


def back(x, y, depth):
    global result
    state = (x, y, tuple(sorted(check)))  # 현재 상태 정의

    if state in memo and memo[state] >= depth:  # 메모이제이션 확인
        return
    memo[state] = depth  # 현재 상태 저장(state가 키, depth가 value)

    result = max(result, depth)

    # 남은 가능한 이동이 현재 최대 깊이를 초과하지 않으면 중단
    if depth + (r * c - len(check)) <= result:
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] not in check:
                check.add(board[nx][ny])
                back(nx, ny, depth + 1)
                check.remove(board[nx][ny])


check.add(board[0][0])
back(0, 0, 1)  # x, y, depth
print(result)
