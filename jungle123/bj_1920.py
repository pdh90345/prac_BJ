# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys, bisect

n = int(input())

A = list(map(int, sys.stdin.readline().split()))

m = int(input())

M = list(map(int, sys.stdin.readline().split()))

A.sort()


def binary_search(A: list, find: int):
    first = 0
    last = len(A) - 1
    while first <= last:
        mid = (first + last) // 2
        if find == A[mid]:
            return 1
        elif find > A[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return 0


for i in range(m):
    print(binary_search(A, M[i]))

# for i in range(m):
#     if M[i] in A:
#         print(1)
#     else:
#         print(0)

# for i in range(m):
#     index = bisect.bisect_left(A, M[i])
#     if index < len(A) and A[index] == M[i]:
#         print(1)
#     else:
#         print(0)
