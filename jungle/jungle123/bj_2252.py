# 첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 회수이다.
# 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

# 첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

indegree = [0] * (n + 1)  # 1번부터 하기위해
adj_list = {i: [] for i in range(1, n + 1)}  # 1번부터 하기위해

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    indegree[b] += 1

# print(adj_list)
# print(indegree)

zero_indegree = deque()  # indegree가 0인 index를 큐에 삽입
for i in range(1, n + 1):
    if indegree[i] == 0:
        zero_indegree.append(i)

result = []
while zero_indegree:
    current = zero_indegree.popleft()
    result.append(current)  # 결과에 저장하고
    for next in adj_list[current]:  # 인접리스트 확인
        indegree[next] -= 1  # indegree 줄이고
        if indegree[next] == 0:  # 0이면 큐에 추가
            zero_indegree.append(next)

for i in result:
    print(i, end=" ")
