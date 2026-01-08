# 쇠막대기

import sys

input = sys.stdin.readline

iron = list(map(str, input().strip()))
stack = []
stack.append(iron[0])
result = 0
for i in range(1, len(iron)):
    if stack and iron[i] == ")" and iron[i - 1] == "(":
        stack.pop()
        result += len(stack)
    elif stack and iron[i] == ")":
        stack.pop()
        result += 1
    else:
        stack.append(iron[i])

print(result)
