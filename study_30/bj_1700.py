# 멀티탭 스케줄링

import sys

n, k = map(int, sys.stdin.readline().split())
product = list(map(int, sys.stdin.readline().split()))

plug = []


count = 0

for i in range(k):
    if product[i] in plug:
        continue
    if len(plug) < n:
        plug.append(product[i])
        continue
    plug_index = [0] * (k + 1)
    max_index = 0

    for j in range(n):
        if plug[j] not in product[i:]:
            plug_index[plug[j]] = 101
        elif plug[j] in product[i:]:
            plug_index[plug[j]] = product[i:].index(plug[j])
        max_index = max(max_index, plug_index[plug[j]])  # 가장 먼 전기제품 확인
    del plug[plug.index(plug_index.index(max_index))]
    plug.append(product[i])
    count += 1
print(count)
