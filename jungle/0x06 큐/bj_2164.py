# 카드2

from collections import deque

n = int(input())
d = deque()

for i in range(1, n + 1):
    d.append(i)

while len(d) > 1:
    d.popleft()
    d.rotate(-1)

print(d[-1])
