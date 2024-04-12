# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

import sys


n, m = map(int, sys.stdin.readline().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i


def find(p: int):
    if parent[p] == p:
        return p
    else:
        parent[p] = find(parent[p])
        return parent[p]


def union(a: int, b: int):
    roota = find(a)
    rootb = find(b)
    if roota < rootb:
        parent[rootb] = roota
    else:
        parent[roota] = rootb


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) != find(b):
        union(a, b)

for i in range(n + 1):
    find(i)

print(len(set(parent[1:])))
