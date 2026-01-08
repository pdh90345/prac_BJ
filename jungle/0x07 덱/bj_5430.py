# AC

import sys
from collections import deque

t = int(input())

for _ in range(t):
    command = list(map(str, sys.stdin.readline().strip()))
    n = int(sys.stdin.readline().strip())
    input_numbers = sys.stdin.readline().strip()
    if input_numbers == "[]":
        d1 = []
    else:
        d1 = deque(map(str, input_numbers.strip("[]").split(",")))
    rcnt = 0
    error = False

    for i in range(len(command)):
        if command[i] == "R":
            rcnt += 1
        elif rcnt % 2 == 0:
            if command[i] == "D":
                if d1:
                    d1.popleft()
                else:
                    print("error")
                    error = True
                    break
        elif rcnt % 2 == 1:
            if command[i] == "D":
                if d1:
                    d1.pop()
                else:
                    print("error")
                    error = True
                    break

    if not error:
        if rcnt % 2 == 1:
            d1.reverse()
        print("[" + ",".join(map(str, d1)) + "]")
