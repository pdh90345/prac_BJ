# 벌집 2

import sys

input = sys.stdin.readline

n = int(input())


max_num = 9 * pow(10, 18)


def tri(i):
    return 6 * (i * (i + 1) // 2) + 1


def find_min_i(n):
    left = 0
    rigth = max_num

    while left < rigth:
        mid = (left + rigth) // 2
        if tri(mid) < n:
            left = mid + 1
        else:
            rigth = mid
    return left + 1  # 1이 0이므로 +1 해준다


print(find_min_i(n))

# for i in range(0, max_num):
#     if n <= tri(i):
#         print(i + 1)
#         break
