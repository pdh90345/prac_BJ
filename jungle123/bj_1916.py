# 최소비용 구하기


import sys
import heapq

n = int(input())
m = int(input())

adj_list = {i: [] for i in range(1, n + 1)}
dist = [100000 * 1000] * (n + 1)
pq = []

for i in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    adj_list[s].append((w, e))

start, end = map(int, input().split())

heapq.heappush(pq, (0, start))
dist[start] = 0
while pq:
    chkDist, now = heapq.heappop(pq)
    if dist[now] < chkDist:
        continue
    for weight, nextVertex in adj_list[now]:
        newDist = chkDist + weight
        if dist[nextVertex] > newDist:
            dist[nextVertex] = newDist
            heapq.heappush(pq, (newDist, nextVertex))

print(dist[end])
