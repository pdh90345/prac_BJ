# 로프

import sys

n = int(input())
rope = []
for i in range(n):
    rope.append(int(sys.stdin.readline().strip()))

rope.sort()

result = 0

for i in range(n):
    current = rope[i] * (n - i)
    result = max(result, current)

print(result)
