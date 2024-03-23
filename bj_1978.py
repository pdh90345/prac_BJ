# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

import sys

N = input()
input_int = list(map(int, sys.stdin.readline().strip().split()))
count = 0
for i in range(int(N)):
    num = input_int[i]
    if num in [2, 3, 5, 7]:
        count += 1
    elif num > 1 and num % 2 != 0:
        is_Prime = True
        for j in range(3, (num // 2) + 1, 2):
            if num % j == 0:
                is_Prime = False
                break
        if is_Prime == True:
            count += 1


print(count)
