# 파티

import sys, heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
hq = []
adj_list = {i: [] for i in range(n + 1)}
adj_list_rev = {i: [] for i in range(n + 1)}

for _ in range(m):
    s, e, w = map(int, input().split())
    adj_list[s].append((w, e))
    adj_list_rev[e].append((w, s))  # x 에서 출발하기 위해 s, e를 뒤집는다

visit1 = [False] * (n + 1)
visit2 = [False] * (n + 1)

dist1 = [sys.maxsize] * (n + 1)
dist2 = [sys.maxsize] * (n + 1)
dist1[x], dist2[x] = 0, 0


def dijk(list, visit, dist):
    heapq.heappush(hq, (0, x))  # 출발 설정을 잘해야 한다
    dist[x] = 0
    while hq:
        cur_w, cur_e = heapq.heappop(hq)
        if visit[cur_e]:
            continue
        visit[cur_e] = True
        for n_w, n_e in list[cur_e]:
            if dist[n_e] > dist[cur_e] + n_w:
                dist[n_e] = dist[cur_e] + n_w
                heapq.heappush(hq, (dist[n_e], n_e))  # 변경된 최소 거리


dijk(adj_list, visit1, dist1)
dijk(adj_list_rev, visit2, dist2)

result = 0
for i in range(1, n + 1):
    result = max(result, dist1[i] + dist2[i])
print(result)
