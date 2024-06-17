# N과 M(4)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0]


def back(depth):
    if depth == m:
        print(*arr[1:])
        return
    for i in range(1, n + 1):
        if i >= arr[-1]:
            arr.append(i)
            back(depth + 1)
            arr.pop()


back(0)
