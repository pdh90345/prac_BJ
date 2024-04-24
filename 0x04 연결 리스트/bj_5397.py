# 키로거

import sys

t = int(input())

s1 = []
s2 = []

for _ in range(t):
    stringL = list(sys.stdin.readline().strip())
    for item in stringL:
        if item == "<":
            if s1:
                s2.append(s1.pop())
        elif item == ">":
            if s2:
                s1.append(s2.pop())
        elif item == "-":
            if s1:
                s1.pop()
        else:
            s1.append(item)
    s1.extend(reversed(s2))
    print("".join(s1))
    s1 = []
    s2 = []
