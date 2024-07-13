# IOIOI

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
S = input().strip()

p1 = "IOI"

for i in range(2, n + 1):
    p1 = p1 + "OI"

index = 0
cnt = 0
while len(S) - len(p1) >= index:
    check = S.find(p1, index)
    if check != -1:
        cnt += 1
        index = check + 1
    else:
        break
print(cnt)
