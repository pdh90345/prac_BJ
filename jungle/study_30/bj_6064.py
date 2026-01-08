# 카잉 달력

import sys, math

input = sys.stdin.readline

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    max_count = math.lcm(m, n)
    count = x
    while count <= max_count:
        # if (count - x) % m == 0:
        if (count - y) % n == 0:
            print(count)
            break
        else:
            count += m
    if count > max_count:
        print(-1)
