# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

import sys

a, b, c = map(int, sys.stdin.readline().split())


# def multi(a, n):
#     if n == 1:
#         return a % c
#     else:
#         tmp = multi(a, n // 2)
#         if n % 2 == 0:
#             return (tmp * tmp) % c
#         else:
#             return (tmp * tmp * a) % c


# print(multi(a, b))

print(pow(a, b, c))
