# 오큰수

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
chk_arr = list(-1 for _ in range(n))

stack = []
for i, value in enumerate(arr):
    # 스택안의 value가 현재 배열의 value 보다 작으면 현재 value가 오큰수 이다.
    while stack and stack[-1][1] < value:
        index = stack.pop()[0]  # 인덱스 뽑아서
        chk_arr[index] = value  # 결과 배열 인덱스에 현재 배열 value 삽입
    stack.append((i, value))

# for i in range(len(chk_arr)):
#     print(chk_arr[i], end=" ")
print(*chk_arr)
