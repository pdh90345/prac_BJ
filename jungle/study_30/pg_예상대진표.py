# 예상 대진표

import sys

input = sys.stdin.readline
n = int(input())


def solution(n, a, b):
    cnt = 1
    while a != b:
        cnt += 1
        a = (a + 1) // 2
        b = (b + 1) // 2

    return cnt - 1
