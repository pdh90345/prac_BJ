# 지름길

import sys, heapq

input = sys.stdin.readline

n, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

hq = []
adj_list = {i: [] for i in range(d + 1)}
dist = [sys.maxsize] * (d + 1)

for i in range(d):
    adj_list[i].append((1, i + 1))


for short in arr:
    s, e, v = map(int, short)
    if e - s > v and e <= d:
        adj_list[s].append((v, e))


def shortcut(list, dist):
    heapq.heappush(hq, (0, 0))
    dist[0] = 0
    while hq:
        cur_w, cur_e = heapq.heappop(hq)
        if cur_w > dist[cur_e]:
            continue
        for n_w, n_e in list[cur_e]:
            if dist[n_e] > cur_w + n_w:
                dist[n_e] = cur_w + n_w
                heapq.heappush(hq, (dist[n_e], n_e))


shortcut(adj_list, dist)
print(dist[d])
