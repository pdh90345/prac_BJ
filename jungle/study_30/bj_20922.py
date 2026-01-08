# 겹치는 건 싫어

import sys

n, k = map(int, input().split())

nums = list(map(int, sys.stdin.readline().split()))

chk_num = [0] * (max(nums) + 1)

s, e = 0, 0
result = 0
while e < n:
    if chk_num[nums[e]] < k:
        chk_num[nums[e]] += 1
        e += 1
    else:
        chk_num[nums[s]] -= 1
        s += 1
    result = max(result, e - s)


print(result)
