# 에디터
# 다시 풀어보기
import sys

s1 = list(map(str, sys.stdin.readline().strip()))
s2 = []
n = int(input())

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())
    if len(command) == 1:
        if command[0] == "L":
            if len(s1) > 0:
                s2.append(s1.pop())
        elif command[0] == "D":
            if len(s2) > 0:
                s1.append(s2.pop())
        elif command[0] == "B":
            if s1:
                s1.pop()
    else:
        s1.append(command[1])

s1.extend(reversed(s2))
print("".join(s1))
