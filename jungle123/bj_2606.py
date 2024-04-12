# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

import sys

sys.setrecursionlimit(10**5)

n = int(input())
m = int(input())

parent = [0] * (n + 1)
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


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) != find(b):
        union(a, b)

result = -1
for i in range(n + 1):
    if find(i) == 1:
        result += 1

print(result)
