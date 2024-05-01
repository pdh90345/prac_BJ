# 옥상 정원 꾸미기

import sys

n = int(input())

building = []
for _ in range(n):
    building.append(int(sys.stdin.readline().strip()))

stack = []
cnt = 0
for i in range(len(building)):
    while stack and stack[-1] <= building[i]:
        stack.pop()
    if not stack:
        stack.append(building[i])
        continue
    else:
        cnt += len(stack)
        stack.append(building[i])

print(cnt)
