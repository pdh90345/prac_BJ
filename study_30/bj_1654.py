# 랜선 자르기

import sys

k, n = map(int, sys.stdin.readline().split())

arr = []
sum = 0
for _ in range(k):
    lan = int(sys.stdin.readline().strip())
    arr.append(lan)
    sum += lan
start = 1
end = sum // n


def b_s(arr, s, e):
    cnt = 0
    while s <= e:
        mid = (s + e) // 2
        for i in range(k):
            cnt += arr[i] // mid
        if cnt < n:
            e = mid - 1
        else:
            s = mid + 1  # 최대값을 찾아야 하므로
        cnt = 0
    return e


ans = b_s(arr, start, end)
print(ans)
