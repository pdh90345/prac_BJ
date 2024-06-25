# 토너먼트

import sys, math


input = sys.stdin.readline
n, kim, lim = map(int, input().split())


def find_round(kim, lim):
    round_num = 0
    while kim != lim:
        kim = (kim + 1) // 2
        lim = (lim + 1) // 2
        round_num += 1
    return round_num


print(find_round(kim, lim))


# # 메모리 초과
# sys.setrecursionlimit(10**5)

# input = sys.stdin.readline
# n, kim, lim = map(int, input().split())


# def find(n, kim, lim):
#     if n % 2 == 1:
#         n = n + 1
#     if kim <= n // 2 and lim > n // 2:
#         result = int(math.ceil(math.log(n, 2)))
#         print(result)
#         exit()

#     else:
#         if kim <= n // 2 and lim <= n // 2:
#             ans = find(n // 2, kim, lim)
#             if ans != None:
#                 return ans
#         else:
#             ans = find(n // 2, kim - n // 2, lim - n // 2)
#             if ans != None:
#                 return ans


# if find(n, kim, lim) == None:
#     print(-1)
# else:
#     print(find(n, kim, lim))
