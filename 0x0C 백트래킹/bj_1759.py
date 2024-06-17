# 암호 만들기

import sys

input = sys.stdin.readline

l, c = map(int, input().split())
alpa = list(map(str, input().split()))

alpa.sort()
check = set()
vowels = ["a", "e", "i", "o", "u"]
result = ["0"]


def back(depth, count):
    if depth == l:
        if 0 < count and l - count > 1:  # 모음 1개 이상, 자음 2개 이상
            print(*result[1:], sep="")
            return
        return
    for i in alpa:
        if i not in check and i > result[-1]:
            result.append(i)
            check.add(i)
            if i in vowels:  # i가 모음일 때
                back(depth + 1, count + 1)
            else:
                back(depth + 1, count)
            check.remove(i)
            result.pop()


back(0, 0)
