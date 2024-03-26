# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오

import sys

list_num = []

n = int(input())

for i in range(n):
    list_num.append(int(sys.stdin.readline().strip()))

list_num.sort()

for i in range(n):
    print(f"{list_num[i]}")
