# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
from collections import deque
import sys

n = int(input())

d = deque()


def push(x: int):
    d.append(x)
    return


def pop():
    if d:
        print(d.popleft())
    else:
        print(-1)
    return


def size():
    print(len(d))
    return


def empty():
    if d:
        print(0)
    else:
        print(1)
    return


def front():
    if d:
        print(d[0])
    else:
        print(-1)


def back():
    if d:
        print(d[-1])
    else:
        print(-1)


for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().strip().split()))
    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    elif cmd[0] == "front":
        front()
    elif cmd[0] == "back":
        back()
    else:
        break
