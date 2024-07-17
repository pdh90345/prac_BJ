# 역원소 정렬

import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
n = arr.pop(0)
inputCnt = len(arr)

while True:
    if inputCnt == n:
        break
    temp = list(map(int, input().split()))
    inputCnt += len(temp)

    arr.extend(temp)

reversed_nums = []
for number in arr:
    reversed_nums.append(int(str(number)[::-1]))

reversed_nums.sort()
print(*reversed_nums, sep="\n")


def reverse(num):
    reversed_number = 0
    while num > 0:
        reversed_number = reversed_number * 10 + num % 10
        num = num // 10
    return reversed_number


reversed_nums = []
for number in arr:
    reversed_nums.append(reverse(number))

reversed_nums.sort()
print(*reversed_nums, sep="\n")
