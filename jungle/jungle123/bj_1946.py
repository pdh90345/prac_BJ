# 신입 사원

import sys

t = int(input())
for _ in range(t):
    n = int(input())
    jr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    jr.sort()
    cnt = 1
    chk = jr[0][1]
    for i in range(1, n):
        if (
            chk > jr[i][1]
        ):  # 서류 1등을 기준으로 면접 등수가 높은사람이 오면 기준점을 그사람으로
            chk = jr[i][1]
            cnt += 1
    print(cnt)
