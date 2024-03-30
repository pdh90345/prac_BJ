# 유니온 파인드 연습해보기

import sys
from collections import deque

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

d = deque()
parent = [0] * (n + 1)

for i in range(m):
    w, s, e = map(int, sys.stdin.readline().split())
    d.append((w, s, e))

for i in range(n + 1):
    parent[i] = i


def find(p: int):
    if parent[p] == p:
        return p
    else:
        parent[p] = find(parent[p])
        return parent[p]


def union(s: int, e: int):
    roots = find(s)
    roote = find(e)
    if roots < roote:
        parent[roote] = roots
    else:
        parent[roots] = roote


for _ in range(m):
    w, s, e = d.popleft()
    if w == 0:
        union(s, e)
    elif w == 1:
        if find(s) == find(e):
            print("YES")
        else:
            print("NO")
