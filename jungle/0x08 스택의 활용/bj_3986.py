# 좋은 단어

import sys

input = sys.stdin.readline


cnt = 0
n = int(input())
for _ in range(n):
    stack = []
    str_arr = list(map(str, input().strip()))
    stack.append(str_arr[0])
    for i in range(1, len(str_arr)):
        if stack and stack[-1] == str_arr[i]:
            stack.pop()
        else:
            stack.append(str_arr[i])
    if not stack:
        cnt += 1

print(cnt)
