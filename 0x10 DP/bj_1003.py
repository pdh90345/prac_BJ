# 피보나치 함수

import sys

input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):
    n = int(input().rstrip())
    if n == 0:
        print(1, 0)
        continue
    dpZero = [0] * (n + 1)
    dpOne = [0] * (n + 1)
    dpZero[0] = 1
    dpOne[0] = 0

    dpZero[1] = 0
    dpOne[1] = 1
    for i in range(2, n + 1):
        dpZero[i] = dpZero[i - 2] + dpZero[i - 1]
        dpOne[i] = dpOne[i - 2] + dpOne[i - 1]
    print(dpZero[n], dpOne[n])
