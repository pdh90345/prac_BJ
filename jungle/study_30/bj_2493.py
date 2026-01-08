# 탑

import sys

n = int(input())

tower = list(map(int, sys.stdin.readline().split()))
tower.insert(0, 0)

s = []

result = [0] * (n + 1)


for i in range(1, n + 1):
    while s:
        if tower[i] < s[-1][1]:
            result[i] = s[-1][0]
            s.append((i, tower[i]))
            break
        else:
            s.pop()
    if not s:
        s.append((i, tower[i]))


for i in range(1, n + 1):
    print(result[i], end=" ")
