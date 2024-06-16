# 트럭

import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())  # 트럭 개수, 다리 길이, 다리 하중
truck = list(map(int, input().split()))  # 트럭 무게

bridge = deque()
for _ in range(w):
    bridge.append(0)  # 트럭이 없으면 0으로 채운다

i = 0  # 트럭 번호
cnt = 0
while bridge:
    out_b = bridge.popleft()  # 다리를 나가는 트럭
    L = L + out_b  # 다리 무게 복원
    if i <= len(truck) - 1:  # 트럭이 남아 있을 때
        if L >= truck[i]:
            bridge.append(truck[i])  # 다리로 트럭을 넣는다
            L = L - truck[i]  # 다리 무게 줄이기
            i += 1
        else:
            bridge.append(0)  # 다리 무게가 트럭보다 작으면 0 추가
    cnt += 1

print(cnt)
