# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
import sys

n = int(input())
stack = []


def push(x: int):
    stack.append(x)
    return


def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)
    return


def size():
    print(len(stack))
    return


def empty():
    if stack:
        print(0)
    else:
        print(1)
    return


def top():
    if stack:
        print(stack[-1])
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
    elif cmd[0] == "top":
        top()
    else:
        break
