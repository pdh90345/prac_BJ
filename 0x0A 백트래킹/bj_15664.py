# N과 M(10)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.insert(0, 0)
numbers.sort()
arr = [0]
check = [0] * (n + 1)
result = []


def back(depth):
    if depth == m:
        if arr[1:] not in result:
            result.append(arr[1:])
        return
    for i in range(1, n + 1):
        if not check[i] and numbers[i] >= arr[-1]:
            check[i] = 1
            arr.append(numbers[i])
            back(depth + 1)
            check[i] = 0
            arr.pop()


back(0)
for i in result:
    print(" ".join(map(str, i)))
