# 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline

maxpoint = 100001
minpoint = 0

n, k = map(int, input().split())

chk_num = [False] * (maxpoint + 1)  # 100001까지 들어가야 하므로
d = deque()


def n_plus(cur):
    return cur + 1


def n_minus(cur):
    return cur - 1


def n_double(cur):
    return cur * 2


def bfs(cur, cnt):
    d.append((cur, cnt))
    chk_num[cur] = True

    while True:
        now, sec = d.popleft()
        if now == k:
            return sec
        else:
            # 이동할 지점의 위치와 방문 표시 확인
            if n_plus(now) <= maxpoint and not chk_num[n_plus(now)]:
                d.append((n_plus(now), sec + 1))
                chk_num[n_plus(now)] = True
            if n_minus(now) >= minpoint and not chk_num[n_minus(now)]:
                d.append((n_minus(now), sec + 1))
                chk_num[n_minus(now)] = True
            if n_double(now) <= maxpoint and not chk_num[n_double(now)]:
                d.append((n_double(now), sec + 1))
                chk_num[n_double(now)] = True


print(bfs(n, 0))
