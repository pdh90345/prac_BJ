# 부등호
# 다시 풀어보기

import sys

k = int(input())
signs = list(map(str, sys.stdin.readline().split()))
signs.insert(0, 0)

chk_num = [False] * (10)

min_ans = ""
max_ans = ""


def check(i, j, sign):
    if sign == "<":
        return i < j
    else:
        return i > j


def dfs(depth, ans):
    global min_ans, max_ans
    if depth == k + 1:  # 그래서 depth는 10일때 완성이 된다
        if min_ans == "":
            min_ans = ans
        else:
            max_ans = ans
        return
    else:
        for i in range(10):
            if not chk_num[i]:
                if depth == 0 or check(ans[-1], str(i), signs[depth]):
                    chk_num[i] = True
                    dfs(depth + 1, ans + str(i))  # depth 올리면서 문자열 추가
                    chk_num[i] = False


dfs(0, "")
print(max_ans)
print(min_ans)
