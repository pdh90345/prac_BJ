# Z

import sys

n, r, c = map(int, sys.stdin.readline().split())


# def func(n, r, c):
#     if n == 0:
#         return 0
#     h = 2 ** (n - 1)

#     if r < h and c < h:
#         return 0 * h * h + func(n - 1, r, c)
#     elif r < h and c >= h:
#         return 1 * h * h + func(n - 1, r, c - h)
#     elif r >= h and c < h:
#         return 2 * h * h + func(n - 1, r - h, c)
#     else:
#         return 3 * h * h + func(n - 1, r - h, c - h)


# print(func(n, r, c))

result = 0
while n != 0:
    n -= 1
    half = 2**n

    if r < half and c < half:  # 2 사분면
        result += 0 * half * half
    elif r < half and c >= half:  # 1 사분면
        result += 1 * half * half
        c -= half
    elif r >= half and c < half:  # 3 사분면
        result += 2 * half * half
        r -= half
    else:  # 4 사분면
        result += 3 * half * half
        r -= half
        c -= half

print(result)
