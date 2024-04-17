# 방 번호

import sys

num = int(sys.stdin.readline().strip())

arr = [0] * 9
while num != 0:
    chk = num % 10
    if chk == 9:
        chk = 6
    arr[chk] += 1
    num //= 10

if arr[6] % 2 == 1:
    arr[6] = arr[6] // 2 + 1
else:
    arr[6] = arr[6] // 2


print(max(arr))
