# 두수의 합

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

x = int(input())

cnt = 0

arr.sort()


s, e = 0, len(arr) - 1
while s < e:
    chk = arr[s] + arr[e]
    if chk == x:
        s += 1
        e -= 1
        cnt += 1
    elif chk > x:
        e -= 1
    else:
        s += 1


# def bs(arr, target):
#     s = 0
#     e = len(arr) - 1
#     while s <= e:
#         mid = (s + e) // 2
#         if target == arr[mid]:
#             return mid
#         elif arr[mid] > target:
#             e = mid - 1
#         elif arr[mid] < target:
#             s = mid + 1
#     return 0


# while arr:
#     a = arr[0]
#     target = x - a
#     b = bs(arr, target)
#     if b == 0:
#         arr.remove(a)
#     else:
#         b = arr[b]
#         arr.remove(a)
#         arr.remove(b)
#         cnt += 1

print(cnt)
