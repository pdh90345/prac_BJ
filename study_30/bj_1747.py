# 소수&팰린드롬

import sys, math

input = sys.stdin.readline

n = int(input())


def isPrime(num):
    if num == 1:  # 1은 소수가 아니다
        return False
    for i in range(2, int(math.sqrt(num)) + 1):  # 제곱근 까지만 체크
        if num % i == 0:
            return False
    return True


def findPrime(x):
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    p = 2
    # 제곱근 까지만 확인
    while p * p <= x:
        # 소수이면
        if primes[p] == True:
            # 해당 소수의 배수는 소수가 아니다
            # p^2 부터 하는 이유는 이전 확인 작업에서 이미 처리되어 있다.
            for i in range(p * p, x + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(x + 1) if primes[p]]


def isPalindrom(num):
    if str(num) == str(num)[::-1]:  # 문자열을 뒤집으면 바로 확인 가능
        return True
    else:
        return False


# while True:
#     if isPrime(n):
#         if isPalindrom(n):
#             print(n)
#             break
#     n += 1

arr = findPrime(1003001)
for p in arr:
    if p >= n and isPalindrom(p):
        break
print(p)
