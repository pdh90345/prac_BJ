# 외판원 순회
# 어느 한도시에서 출발해 N개의 도시를 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로. 단, 한 번 갔던 도시는 다시 갈수 없다, 가장 적은 비용
# 비용은 행렬 W[i][j] 형태, 도시 이동 안되면 0

# 첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 다음 N개의 줄에는 비용 행렬이 주어진다. 각 행렬의 성분은 1,000,000 이하의 양의 정수이며,
# 갈 수 없는 경우는 0이 주어진다. W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

# 항상 순회할 수 있는 경우만 입력으로 주어진다.

# 첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.

import sys

n = int(input())

W = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

checked = [0] * n
minValue = sys.maxsize


def dfs(cur: int, count: int, value: int):  # (현재위치, 방문한 노드수, 값)
    global minValue
    if count == n:
        if W[cur][0]:
            minValue = min(value + W[cur][0], minValue)
            return
    for i in range(n):
        if checked[i] == 0 and W[cur][i] and value < minValue:
            checked[i] = 1
            value = value + W[cur][i]
            dfs(i, count + 1, value)
            checked[i] = 0
            value = value - W[cur][i]


checked[0] = 1
dfs(0, 1, 0)
print(minValue)
