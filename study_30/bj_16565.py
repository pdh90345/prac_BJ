# N 포커

import sys
from math import comb

input = sys.stdin.readline

n = int(input().strip())
result = 0
sign = 1

if n == 1 or n == 2 or n == 3:  # 3이하면 0
    print(0)
elif n == 52:  # 52면 1
    print(1)
else:
    for i in range(1, n // 4 + 1):
        fourCardCnt = comb(13, i)  # 4카드 개수
        anotherCardCnt = comb(52 - i * 4, n - i * 4)  # 4카드 뽑고 나머지 개수
        result += sign * fourCardCnt * anotherCardCnt  # 결과 저장
        sign *= -1  # 짝수일 때마다 부호를 바꿔준다(포함-배제 원리)
    print(result % 10007)
