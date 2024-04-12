# 다시 풀어보기


import sys
from collections import deque

n = int(input())
m = int(input())

adj_list = {i: [] for i in range(1, n + 1)}
indegree = [0] * (n + 1)
d = deque()
need = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    adj_list[y].append(
        (x, k)
    )  # 방향 설정을 생각하자 1은 5를 만들때 2개가 필요하다 -> 1은 인디그리가 없지만 5는 인디그리가 있다.
    indegree[x] += 1

# print(adj_list)
# print(indegree)

for i in range(1, n + 1):
    if indegree[i] == 0:
        d.append(i)

while d:
    cur = d.popleft()
    for next, cnt in adj_list[cur]:
        if need[cur].count(0) == n + 1:
            need[next][cur] += cnt
        else:
            for i in range(1, n + 1):
                need[next][i] += need[cur][i] * cnt
        indegree[next] -= 1
        if indegree[next] == 0:
            d.append(next)

for x in enumerate(need[n]):
    if x[1] > 0:
        print(*x)
