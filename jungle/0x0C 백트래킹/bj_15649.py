# N과 M(1)

import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())


def back(depth):
    if depth == m:
        print(*arr)
        return
    for i in range(1, n + 1):
        if i not in check:
            check.add(i)
            arr.append(i)
            back(depth + 1)
            check.remove(i)
            arr.remove(i)


arr = []
check = set()
back(0)

# perm = list(permutations(range(1, n + 1), m))
# perm.sort()

# for item in perm:
#     str_item = " ".join(map(str, item))
#     print(str_item)
