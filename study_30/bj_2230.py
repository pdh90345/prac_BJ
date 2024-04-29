# 수 고르기
import sys

n, m = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

s = 0
e = 1
result = sys.maxsize
while e < len(arr):
    chkSub = arr[e] - arr[s]
    if chkSub < m:
        e += 1
    elif chkSub > m:
        s += 1
        result = min(result, chkSub)
    else:
        result = chkSub
        break

print(result)
