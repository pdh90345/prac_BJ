# 이분 그래프

# 다시 풀어보기

import sys

sys.setrecursionlimit(10**5)

K = int(input())


def dfs(start: int, c: str):
    color[start] = c
    isused[start] = True
    for vertex in adj_list[start]:
        if isused[vertex] == False:
            if c == "r":
                if not dfs(vertex, "b"):
                    return False
            else:
                if not dfs(vertex, "r"):
                    return False
        elif color[vertex] == c:
            return False
    return True


for _ in range(K):
    v, e = map(int, sys.stdin.readline().split())
    isused = [False] * (v + 1)
    color = [None] * (v + 1)
    adj_list = {i: [] for i in range(1, v + 1)}
    for _ in range(e):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    isBiprtite = True
    for i in range(1, v + 1):  # 모든 정점이 다 이어지지 않을수도 있다. 각 정점마다 찾기
        if not isused[i]:
            if not dfs(i, "r"):
                isBiprtite = False
                break
    print("YES" if isBiprtite else "NO")
