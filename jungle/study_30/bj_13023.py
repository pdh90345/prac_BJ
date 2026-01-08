# ABCDE

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

adj_list = {i: [] for i in range(n)}

for i in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def dfs(depth, start):
    if depth == 4:
        return 1
    else:
        visited.add(start)
        for i in adj_list[start]:
            if (
                i not in visited
            ):  # 방문 확인을 연결리스트 들어와서 하면 시간이 더 조금 걸린다
                result = dfs(depth + 1, i)
                if result == 1:
                    return 1
        visited.remove(start)


result = None
for i in range(n):
    visited = set()
    result = dfs(0, i)
    if result == 1:
        break

if result == 1:
    print(1)
else:
    print(0)
