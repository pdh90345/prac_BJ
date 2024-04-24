# 요세푸스 문제

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

d = deque(range(1, n + 1))

cnt = 1
result = []
while d:
    for i in range(1, k):
        d.append(d.popleft())
    result.append(d.popleft())


result = list(map(str, result))
print("<" + ", ".join(result) + ">")

# from collections import deque

# n, k = map(int, input().split())  # 예시로 입력 받는 부분, 실제 환경에서는 sys.stdin.readline() 사용

# d = deque(range(1, n + 1))
# result = []

# while d:
#     d.rotate(-(k-1))  # k-1만큼 왼쪽으로 회전 (k번째 원소를 맨 앞으로)
#     result.append(d.popleft())  # 맨 앞의 원소를 결과 리스트에 추가

# result = list(map(str, result))
# print("<" + ", ".join(result) + ">")
