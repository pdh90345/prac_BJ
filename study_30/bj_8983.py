# 사냥꾼

import sys

n, m, l = map(int, sys.stdin.readline().split())
sands = list(map(int, sys.stdin.readline().split()))
animals = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
cnt = 0
sands.sort()


def binary_search(arr, target):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return e


for i in range(m):
    idx = binary_search(sands, animals[i][0])

    dist = abs(sands[idx] - animals[i][0]) + animals[i][1]
    if idx < n - 1:
        dist_right = abs(sands[idx + 1] - animals[i][0]) + animals[i][1]
    else:
        dist_right = sys.maxsize
    dist = min(dist, dist_right)

    if l >= dist:
        cnt += 1

print(cnt)
