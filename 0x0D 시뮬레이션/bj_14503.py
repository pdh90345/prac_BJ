# 로봇 청소기

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]  # 상 좌 하 우
dy = [0, -1, 0, 1]

dir = deque()
for i in range(4):  # 방향 지정
    dir.append(i)
if d != 0:
    dir.rotate(d)


cnt = 0
q = deque()

q.append((r, c))
while q:
    x, y = q.popleft()
    if room[x][y] == 0:  # 청소 (1)
        room[x][y] = 2
        cnt += 1
    if (  # 주변 4칸 중 청소되지 않은 칸이 있을 때 (3)
        room[x - 1][y] == 0
        or room[x][y - 1] == 0
        or room[x + 1][y] == 0
        or room[x][y + 1] == 0
    ):
        dir.rotate(-1)  # 반시계로 회전 (3-1)
        if room[x + dx[dir[0]]][y + dy[dir[0]]] == 0:  # 청소되지 않은 칸이면 (3-2)
            q.append((x + dx[dir[0]], y + dy[dir[0]]))  # 전진 (3-3)
        else:  # 아니면
            q.append((x, y))  # 가만히 있는다 (3-3)
        continue
    if (  # 청소가 다 되어 있으면 (2)
        room[x - 1][y] != 0
        and room[x][y - 1] != 0
        and room[x + 1][y] != 0
        and room[x][y + 1] != 0
    ):
        if room[x + dx[dir[2]]][y + dy[dir[2]]] == 1:  # 뒤에 벽이 있으면 종료 (2-2)
            break
        else:
            q.append((x + dx[dir[2]], y + dy[dir[2]]))  # 아니면 후진 (2-1)

print(cnt)
