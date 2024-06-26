# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

adjList = {i: [] for i in range(1, n + 1)}
for i in range(m):  # 친구 등록
    s, e = map(int, input().split())
    adjList[s].append(e)
    adjList[e].append(s)


def findFriend(s: int):
    chkList = [0] * (n + 1)
    d = deque()
    for f in adjList[s]:
        d.append((0, f))
    while d:
        cnt, end = d.popleft()
        if chkList[end] == 0:  # 친구 체크 안했을 때만 진행
            chkList[end] = cnt + 1
            for other in adjList[end]:
                if other != s:  # 내 자신이 아닐 경우에만 큐에 삽입
                    d.append((cnt + 1, other))
    return sum(chkList)


resultList = [sys.maxsize] * (n + 1)
for i in range(1, n + 1):
    ans = findFriend(i)
    resultList[i] = ans

print(resultList.index(min(resultList)))  # 가장 작은 값의 인덱스 출력
