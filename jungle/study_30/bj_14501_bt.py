# 퇴사

import sys

input = sys.stdin.readline

n = int(input())
T = [0] * (n + 1)
V = [0] * (n + 1)

for i in range(1, n + 1):
    t, v = map(int, input().split())
    T[i] = t
    V[i] = v

result = 0


def backtracking(depth, date, value):
    global result
    if depth == (n + 1):
        if date == 0:
            result = max(result, value)
    else:
        if depth == 1:
            backtracking(depth + 1, T[depth] - 1, V[depth])
            backtracking(depth + 1, date, value)
        else:
            if date > 0:
                date -= 1
                backtracking(depth + 1, date, value)
            else:
                backtracking(depth + 1, T[depth] - 1, value + V[depth])
            backtracking(depth + 1, date, value)


backtracking(1, 0, 0)
print(result)
