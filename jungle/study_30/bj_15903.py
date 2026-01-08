# 카드 합체 놀이

import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# hq = []
# for i in range(len(arr)):
#     heappush(hq, arr[i])

# for i in range(m):
#     a, b = heappop(hq), heappop(hq)
#     temp = a + b
#     heappush(hq, temp)
#     heappush(hq, temp)

# result = 0
# while hq:
#     result += heappop(hq)

# print(result)

hq = arr
heapify(hq)  # 리스트를 heap으로 변경

for i in range(m):
    a, b = heappop(hq), heappop(hq)
    temp = a + b
    heappush(hq, temp)
    heappush(hq, temp)
print(sum(hq))  # heap도 sum 가능
"""
(function) def sum(
    iterable: Iterable[_SupportsSumNoDefaultT@sum],
    /
) -> (_SupportsSumNoDefaultT@sum | Literal[0])
"""
