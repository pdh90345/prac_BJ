# X보다 작은 수

import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(n):
    if x > arr[i]:
        result.append(arr[i])
for item in result:
    print(item, end=" ")
