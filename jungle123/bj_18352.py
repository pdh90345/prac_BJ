# 특정 거리의 도시 찾기

import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())

adj_list = {i: [] for i in range(1, n + 1)}
visit = [0] * (n + 1)
dist = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)

d = deque()

d.append(x)
visit[x] = 1
dist[x] = 0
while d:
    now = d.popleft()
    chkDist = dist[now]
    for vertex in adj_list[now]:
        if visit[vertex] == 0:
            visit[vertex] = 1
            dist[vertex] = chkDist + 1
            d.append(vertex)

found = False
for index, value in enumerate(dist):
    if value == k:
        print(index)
        found = True
if not found:
    print(-1)
