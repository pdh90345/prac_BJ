# 수리공 항승

import sys

input = sys.stdin.readline

n, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
cnt = 0
tapeIndex = 0

for item in arr:
    if item > tapeIndex:
        tapeIndex = item + l - 1
        cnt += 1

print(cnt)
