# 참외밭

import sys

from collections import defaultdict  # 알아둘 만한 딕셔너리

input = sys.stdin.readline

k = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

dict = defaultdict(list)
for i in range(len(arr)):
    d, side = map(int, arr[i])
    dict[d].append(side)

for i in range(1, 5):
    if len(dict[i]) == 1:
        if i == 1 or i == 2:
            xIndex = i
            x = dict.pop(i)
        else:
            yIndex = i
            y = dict.pop(i)

for index, (dictIndex, value) in enumerate(arr):
    if dictIndex == xIndex or dictIndex == yIndex:
        # (-1 % 6) = (-1 + 6) % 6 = 5 % 6 = 5
        prevIndex = (index - 1) % 6
        nextIndex = (index + 1) % 6
        if arr[prevIndex][0] == xIndex or arr[prevIndex][0] == yIndex:
            smallIndex1, smallValue1 = arr[nextIndex][0], arr[nextIndex][1]
        elif arr[nextIndex][0] == xIndex or arr[nextIndex][0] == yIndex:
            smallIndex2, smallValue2 = arr[prevIndex][0], arr[prevIndex][1]

result = []
for key, values in dict.items():
    for value in values:
        if (key == smallIndex1 and value == smallValue1) or (
            key == smallIndex2 and value == smallValue2
        ):
            continue
        else:
            result.append(value)

# ????
if len(result) < 2:
    result = [1, 1]

size = x[0] * y[0] - result[0] * result[1]
print(size * k)
