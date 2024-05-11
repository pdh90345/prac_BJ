# 휴게소 세우기

import sys

n, m, l = map(int, sys.stdin.readline().split())
highway = list(map(int, sys.stdin.readline().split()))

highway.insert(0, 0)
highway.append(l)
highway.sort()

s = 1
e = l - 1
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(1, len(highway)):
        distance = highway[i] - highway[i - 1]
        if distance > mid:
            cnt += (
                distance - 1
            ) // mid  # 휴게소있는 곳에 하나 더 넣는 것을 피하기 위해서
    if cnt > m:
        s = mid + 1
    elif cnt <= m:
        e = mid - 1
        ans = mid
print(ans)
