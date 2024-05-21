# 두 용액

import sys

input = sys.stdin.readline

n = int(input())
numbers = set(list(map(int, input().split())))
numbers = sorted(numbers)

res1 = numbers[0]
res2 = numbers[len(numbers) - 1]
prev_check = sys.maxsize


def b_s(start, end):
    global res1, res2, prev_check
    while start != end:
        check = numbers[start] + numbers[end]
        if prev_check > abs(check):
            prev_check = abs(check)
            res1 = numbers[start]
            res2 = numbers[end]
        if check == 0:
            res1 = numbers[start]
            res2 = numbers[end]
            return
        elif check > 0:
            end -= 1
        else:
            start += 1
    return


b_s(0, len(numbers) - 1)

print(res1, res2)
