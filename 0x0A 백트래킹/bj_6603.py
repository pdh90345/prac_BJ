# 로또

import sys
from itertools import combinations

input = sys.stdin.readline


def back(depth):
    global check
    if depth == 6:
        print(*result[1:])
        return
    for i in S:
        if i not in check and result[-1] < i:
            check.add(i)
            result.append(i)
            back(depth + 1)
            check.remove(i)
            result.pop()


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    check = set()
    result = [0]
    k = arr[0]
    S = arr[1:]
    back(0)
    print("")

# while True: # 조합
#     arr = list(map(int, input().split()))
#     if arr[0] == 0:
#         break
#     k = arr[0]
#     S = arr[1:]
#     result = list(combinations(S, 6))
#     for item in result:
#         print(" ".join(map(str, item)))
#     print("")
