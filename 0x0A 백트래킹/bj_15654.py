# N과 M(5)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []
check = set()


def back(depth):
    if depth == m:
        print(*arr)
        return
    for i in numbers:
        if i not in check:
            check.add(i)
            arr.append(i)
            back(depth + 1)
            check.remove(i)
            arr.remove(i)


back(0)
