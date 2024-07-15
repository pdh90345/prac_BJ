# 시리얼 번호

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    serial = input().rstrip()
    cnt = 0
    for i in range(len(serial)):
        if ord("1") <= ord(serial[i]) <= ord("9"):
            cnt += ord(serial[i]) - ord("0")

    arr.append([serial, len(serial), cnt])

result = sorted(arr, key=lambda x: (x[1], x[2], x[0]))
for i in range(n):
    print(result[i][0])


# def serial_sum(serial):
#     """시리얼 번호에 포함된 숫자들의 합을 계산"""
#     return sum(int(char) for char in serial if char.isdigit())

# def custom_sort(serial):
#     """정렬 기준을 위한 튜플을 반환"""
#     return (len(serial), serial_sum(serial), serial)

# 정렬
# sorted_serial_numbers = sorted(serial_numbers, key=custom_sort)
