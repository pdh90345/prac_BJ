# 회전하는 큐

import sys
from collections import deque

n, m = map(int, input().split())

arr = deque(i for i in range(1, n + 1))

numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(m):
    mid = (len(arr) - 1) // 2
    chk_index = arr.index(numbers[i])
    if chk_index > mid:
        while numbers[i] != arr[0]:
            arr.rotate(1)
            cnt += 1
        arr.popleft()
    else:
        while numbers[i] != arr[0]:
            arr.rotate(-1)
            cnt += 1
        arr.popleft()

print(cnt)
