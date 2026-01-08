# 타노스

import sys

input = sys.stdin.readline

arr = list(map(int, input().strip()))

oneCnt = arr.count(1) // 2
allOne = arr.count(1)

zeroCnt = arr.count(0) // 2


result = []
for item in arr:
    if zeroCnt > 0:
        if item == 0:
            result.append(item)
            zeroCnt -= 1
        else:
            if allOne > arr.count(1) // 2:
                allOne -= 1
                continue
            else:
                result.append(item)
                oneCnt -= 1

    elif oneCnt > 0 and item == 1:
        result.append(item)
        oneCnt -= 1

print(*result, sep="")
