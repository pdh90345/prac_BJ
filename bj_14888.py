# 연산자 끼워넣기

# 한번 더 풀어보기
import sys

sys.setrecursionlimit(10**5)

n = int(input())

operand = list(map(int, sys.stdin.readline().split()))

operator = list(map(int, sys.stdin.readline().split()))

Min = sys.maxsize
Max = -sys.maxsize


def dfs(num: int, cnt: int):  # cnt는 첨에 수가 들어가기 때문에 1부터
    global Max, Min
    if cnt == n:
        Max = max(num, Max)
        Min = min(num, Min)

    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1

            if i == 0:
                dfs(num + operand[cnt], cnt + 1)
            elif i == 1:
                dfs(num - operand[cnt], cnt + 1)
            elif i == 2:
                dfs(num * operand[cnt], cnt + 1)
            elif i == 3:
                if num < 0:
                    dfs(-((-num) // operand[cnt]), cnt + 1)
                else:
                    dfs(num // operand[cnt], cnt + 1)
            operator[i] += 1


dfs(operand[0], 1)
print(Max, Min)
