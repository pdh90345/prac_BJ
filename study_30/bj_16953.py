# A -> B

import sys

a, b = map(int, sys.stdin.readline().split())


cnt = 1

while b > a:
    if b % 2 == 0 or b % 10 == 1:
        if b % 10 == 1:
            b = b // 10
            cnt += 1
        else:
            b = b // 2
            cnt += 1
    else:
        break
if a == b:
    print(cnt)
else:
    print(-1)
