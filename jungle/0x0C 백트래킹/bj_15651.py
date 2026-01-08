# N과 M(3)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []


def back(depth):
    if depth == m:
        print(*arr)
        return
    for i in range(1, n + 1):
        arr.append(i)
        back(depth + 1)
        arr.pop()


back(0)
