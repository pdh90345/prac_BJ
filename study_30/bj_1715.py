# 카드 정렬하기

import sys
import heapq

n = int(input())
hq = []
for _ in range(n):
    heapq.heappush(hq, int(sys.stdin.readline().strip()))

ans = 0
new_num = 0

while hq:
    if len(hq) == 1:
        break
    else:
        new_num += heapq.heappop(hq)
        new_num += heapq.heappop(hq)
    ans += new_num
    if hq:
        heapq.heappush(hq, new_num)
    new_num = 0

print(ans)
