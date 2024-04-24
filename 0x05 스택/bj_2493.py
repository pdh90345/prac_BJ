# 탑

import sys

n = int(input())

stack = []

tower = list(map(int, sys.stdin.readline().split()))

tower.insert(0, 0)

result = [0] * (n + 1)
chk = 0
for i in range(1, n + 1):
    if not stack:
        stack.append((tower[i], i))
        result[i] = 0
    elif stack[-1][0] <= tower[i]:
        while stack and stack[-1][0] < tower[i]:
            stack.pop()
        if stack:
            chk = stack[-1][1]
            result[i] = chk
        else:
            result[i] = 0
        stack.append((tower[i], i))
    else:
        chk = stack[-1][1]
        result[i] = chk
        stack.append((tower[i], i))

for i in range(1, n + 1):
    print(result[i], end=" ")
