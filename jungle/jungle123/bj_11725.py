# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

import sys
from collections import deque

sys.setrecursionlimit(10**6)
n = int(input())

d = deque()
parent = [0] * (n + 1)
isused = [False] * (n + 1)

adj_list = {i: [] for i in range(1, n + 1)}


for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def bfs(start: int):
    isused[start] = True
    d.append(start)
    while d:
        node = d.popleft()
        for vertex in adj_list[node]:
            if isused[vertex] != True:
                isused[vertex] = True
                parent[vertex] = node
                d.append(vertex)


def dfs(start: int):
    if isused[start] == True:
        return
    isused[start] = True
    for vertex in adj_list[start]:
        if isused[vertex] != True:
            parent[vertex] = start
            dfs(vertex)


# bfs(1)
dfs(1)
for i in range(2, n + 1):
    print(parent[i])
