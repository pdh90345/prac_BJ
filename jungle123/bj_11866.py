# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)
# 예제와 같이 요세푸스 순열을 출력한다.
from collections import deque

n, k = list(map(int, input().split()))
d = deque()
for i in range(1, n + 1):
    d.append(i)

result = []
for i in range(n):
    d.rotate(-(k - 1))
    result.append(d.popleft())

print(f"<{', ' .join(map(str, result))}>")
