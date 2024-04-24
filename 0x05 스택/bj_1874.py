# 스택 수열

import sys

n = int(input())
stack = []
chk = 0
possible = True
result = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())

    while chk < num:
        chk += 1
        stack.append(chk)
        result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        possible = False
        break


if possible:
    for item in result:
        print(item)
