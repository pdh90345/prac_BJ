# 피보나치 2

n = int(input())

F = [0] * (n + 1)


# def fibo(n: int):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif F[n] != 0:
#         return F[n]
#     else:
#         F[n] = fibo(n - 1) + fibo(n - 2)
#     return F[n]


# print(fibo(n))


def fibo2(n: int):
    F[0] = 0
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


print(fibo2(n))
