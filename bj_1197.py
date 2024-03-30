# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

# 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

# 다시 해보기

import heapq, sys

n, m = map(int, input().split())
pq = []  # 가중치 우선순위 큐
parent = [0] * (n + 1)  # 부모 노드 배열(1부터 시작)

for i in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    heapq.heappush(pq, (w, s, e))  # 가중치가 낮은 것 부터 넣는다

for i in range(1, n + 1):
    parent[i] = i


def find(p: int):
    if parent[p] == p:  # 부모가 같으면 그대로
        return p
    else:
        parent[p] = find(parent[p])  # 아니면 부모를 찾아서 저장 (경로 압축)
        return parent[p]


def union(s: int, e: int):
    root1 = find(s)
    root2 = find(e)
    if root1 < root2:  # 부모가 작으면 작은 것이 부모가 된다 (방향이 따로 없어도 됨)
        parent[root2] = root1
    else:
        parent[root1] = root2


useEdge = 0
result = 0

while useEdge < n - 1:  # 간선은 노드 - 1개
    w, s, e = heapq.heappop(pq)
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1

print(result)
