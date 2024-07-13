# 회전 초밥

import sys
from collections import deque

input = sys.stdin.readline


n, d, k, c = map(int, input().split())

plates = set()
d = deque()
arr = []
for i in range(n):
    if i < k:
        d.append(int(input().strip()))
        plates.add(d[-1])
        continue
    arr.append(int(input().strip()))

# 처음 d개를 나중에 담는다
for item in d:
    arr.append(int(item))

if c in plates:
    ans = len(plates)
else:
    ans = len(plates) + 1

for i in range(n - 1):
    out = d.popleft()
    plates.remove(out)
    if out in d:
        plates.add(out)

    d.append(arr[i])
    plates.add(arr[i])

    if c in plates:
        temp = len(plates)
    else:
        temp = len(plates) + 1

    ans = max(ans, temp)

print(ans)
