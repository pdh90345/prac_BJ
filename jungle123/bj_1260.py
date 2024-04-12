# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

import sys
from collections import deque

sys.setrecursionlimit(10**5)

n, m, v = map(int, sys.stdin.readline().split())

adj_list = {i: [] for i in range(1, n + 1)}  # 인접리스트 초기화
isusedDFS = [False] * (n + 1)
isusedBFS = [False] * (n + 1)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for key in adj_list:
    adj_list[key].sort()


def dfs(key: int):
    if isusedDFS[key] == True:
        return
    isusedDFS[key] = True
    print(key, end=" ")
    for i in range(len(adj_list[key])):
        dfs(adj_list[key][i])


d = deque()


def bfs(key: int):
    d.append(key)
    isusedBFS[key] = True
    while d:
        key = d.popleft()
        print(key, end=" ")
        for vertex in adj_list[key]:
            if isusedBFS[vertex] != True:
                d.append(vertex)
                isusedBFS[vertex] = True


dfs(v)
print()
bfs(v)
