# 아침 산책

# 정점과 간선의 규칙을 이해하자

import sys

sys.setrecursionlimit(10**6)

n = int(input())

strA = str(sys.stdin.readline().strip())
isused = [False] * (n + 1)
vertex_list = [0] + list(strA)

adj_list = {i: [] for i in range(1, n + 1)}

chk = 0
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
    if vertex_list[u] == "1" and vertex_list[v] == "1":
        chk += 2

cnt = 0


def dfs(start: int):
    global cnt
    isused[start] = True
    for vertex in adj_list[start]:
        if isused[vertex] == False:
            if vertex_list[vertex] == "1":
                cnt += 1
            else:
                dfs(vertex)
    return cnt


sum = 0
for i in range(1, n + 1):
    if vertex_list[i] == "0" and isused[i] != True:
        rs = dfs(i)
        sum += rs * (rs - 1)
        cnt = 0


print(sum + chk)


# 시간 초과
# def dfs(start: int):
#     global cnt
#     isused[start] = True
#     for vertex in adj_list[start]:
#         if isused[vertex] == False:
#             if vertex_list[vertex] == "1":
#                 isused[vertex] = True
#                 cnt += 1
#             else:
#                 dfs(vertex)


# for i in range(1, n + 1):
#     if vertex_list[i] == "1":
#         isused = [False] * (n + 1)
#         dfs(i)

# print(cnt)
