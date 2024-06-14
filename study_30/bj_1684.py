# 같은 나머지


import sys, math

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

new_numbers = []
for i in range(len(numbers) - 1):
    for j in range(1, len(numbers)):
        new_numbers.append(abs(numbers[i] - numbers[j]))

ans = new_numbers[0]
for i in range(1, len(new_numbers)):
    ans = math.gcd(ans, new_numbers[i])
print(ans)


# if n == 1:
#     print(numbers[0])
#     exit()

# new_numbers = []
# for number in numbers:
#     number = abs(number)
#     new_numbers.append(number)

# new_numbers.sort()
# ans = new_numbers[0]
# new_numbers = numbers
# for i in range(1, len(new_numbers)):
#     ans = math.gcd(ans, new_numbers[i])


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True


# result = ans
# R1 = 0
# R2 = 0
# out = False
# for i in range(new_numbers[0], ans - 1, -1):
#     if is_prime(i):
#         cnt = 1
#         R1 = round(new_numbers[0] / i - new_numbers[0] // i, 6)
#         for j in range(1, len(new_numbers)):
#             R2 = round(new_numbers[j] / i - new_numbers[j] // i, 6)
#             if R1 != R2:
#                 continue
#             else:
#                 cnt += 1
#             if cnt == len(new_numbers):
#                 result = i
#                 out = True
#                 break
#     if out == True:
#         break

# print(result)
