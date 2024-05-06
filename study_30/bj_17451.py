# 평행 우주

import sys

n = int(input())
planets = list(map(int, sys.stdin.readline().split()))

planets.reverse()
speed = 0

for i in range(n):
    if speed <= planets[i]:
        speed = planets[i]
    else:
        if speed % planets[i] != 0:
            speed = ((speed // planets[i]) + 1) * planets[i]

print(speed)
