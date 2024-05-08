# 트리의 지름

import sys

sys.setrecursionlimit(10**5)

n = int(input())

adj_list = {i: [] for i in range(1, n + 1)}

visited = [-1] * (n + 1)

for _ in range(n - 1):  # 트리는 항상 node - 1 개의 간선을 가짐
    p, c, w = map(int, sys.stdin.readline().split())
    adj_list[p].append((c, w))
    adj_list[c].append((p, w))

result = 0


def dfs(node, chk_w):
    for adj_node in adj_list[node]:
        if visited[adj_node[0]] == -1:
            visited[adj_node[0]] = chk_w + adj_node[1]
            dfs(adj_node[0], chk_w + adj_node[1])


visited[1] = 0
dfs(1, 0)

last_node = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[last_node] = 0
dfs(last_node, 0)
print(max(visited))
