# 계란으로 계란깨기

import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
S = [0] * n
W = [0] * n
for i in range(n):
    S[i], W[i] = map(int, input().split())

result = 0
check = set()  # 깨진 계란 체크


def back(depth, count):
    global result
    if depth == n:
        result = max(result, count)
        return
    else:
        if depth in check:  # 현재 계란이 깨진 계란일 때
            back(depth + 1, count)
        elif len(check) == n - 1:  # 하나빼고 나머지 계란이 다 깨져 있을 때
            back(depth + 1, count)
        else:
            for i in range(n):
                if i == depth or S[i] <= 0:  # 손에 든 계란 이거나 깨진 계란이면 스킵
                    continue
                S[i] = S[i] - W[depth]
                if S[i] <= 0:  # 바닥에 있는 계란이 깨지면 추가
                    check.add(i)
                S[depth] = S[depth] - W[i]
                if S[depth] <= 0:  # 손에든 계란이 깨지면 추가
                    check.add(depth)
                if S[i] <= 0 and S[depth] <= 0:  # 두개 다 깨졌을 때
                    back(depth + 1, count + 2)
                elif S[i] > 0 and S[depth] > 0:  # 두개 다 안깨졌을 때
                    back(depth + 1, count)
                else:  # 한개만 깨졌을 때
                    back(depth + 1, count + 1)
                if S[i] <= 0:  # 행동 취소
                    check.remove(i)
                S[i] = S[i] + W[depth]
                if S[depth] <= 0:  # 행동 취소
                    check.remove(depth)
                S[depth] = S[depth] + W[i]


back(0, 0)
print(result)
