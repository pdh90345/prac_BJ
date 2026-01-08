# 후보 추천하기

import sys

input = sys.stdin.readline

n = int(input())
cnt = int(input())
arr = list(map(int, input().split()))

candidates = {}
for i in range(len(arr)):
    if len(candidates) < n:
        if arr[i] in candidates.keys():
            candidates[arr[i]][0] = candidates[arr[i]][0] + 1
            continue
        candidates[arr[i]] = [1, i]
        continue
    if arr[i] in candidates.keys():
        candidates[arr[i]][0] = candidates[arr[i]][0] + 1
    else:
        # candidates.values()는 [[1, 2], [3, 1], [2, 2]]를 반환합니다.
        # min(..., key=lambda x: x[0])는 각 리스트의 첫 번째 요소(추천 수)를 기준으로 최소값을 찾습니다. 여기서는 [1, 2]가 선택됩니다.
        # [1, 2][0]는 1을 반환합니다.

        # min(candidates.values(), key=lambda x: x[0])
        # 이건 최소값을 반환하는것이 아니라 x[0]이 가장 작은 value를 반환 즉 리스트를 반환한다.
        min_v = min(candidates.values(), key=lambda x: x[0])[0]  # 추천수, 인덱스 순
        min_list = list(filter(lambda x: x[1][0] == min_v, candidates.items()))

        victim = min(min_list, key=lambda x: x[1][1])[0]
        del candidates[victim]
        candidates[arr[i]] = [1, i]

result = sorted(candidates.keys())
print(*result)
