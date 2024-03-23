# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

import sys


def is_Prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    a, b = n // 2, n // 2
    while a > 0:
        if is_Prime(a) and is_Prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
