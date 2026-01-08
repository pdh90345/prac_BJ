# 제로

import sys

k = int(input())
result = []
for _ in range(k):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        result.pop()
    else:
        result.append(num)

sum_num = 0
for item in result:
    sum_num += item

print(sum_num)
