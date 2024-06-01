# N과 M(2)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0]
check = set()


def back(depth):
    if depth == m:
        print(*arr[1:])
        return
    for i in range(1, n + 1):
        if i not in check and i > arr[-1]:
            check.add(i)
            arr.append(i)
            back(depth + 1)
            check.remove(i)
            arr.remove(i)


back(0)
