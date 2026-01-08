# 수 이어쓰기

import sys

input = sys.stdin.readline

nums = list(map(str, input().strip()))
n = 0  # 증가 하는 수
idx = 0  # 리스트의 인덱스
check = True
while check:
    n += 1
    s = str(n)
    for i in s:  # 문자열은 in이 가능하다
        if nums[idx] == i:
            idx += 1
            if idx == len(nums):
                check = False
                break

print(n)
