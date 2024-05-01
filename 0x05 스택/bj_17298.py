# 오큰수

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
chk_arr = list(-1 for _ in range(n))

stack = []
for i, value in enumerate(arr):
    while stack and stack[-1][1] < value:
        index = stack.pop()[0]
        chk_arr[index] = value
    stack.append((i, value))

# for i in range(len(chk_arr)):
#     print(chk_arr[i], end=" ")
print(*chk_arr)
