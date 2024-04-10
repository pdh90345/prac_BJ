# 동전 0

import sys

n, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(sys.stdin.readline().strip()))

cnt = 0

for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if A[i] <= k:
        cnt += k // A[i]
        k = k % A[i]

print(cnt)
