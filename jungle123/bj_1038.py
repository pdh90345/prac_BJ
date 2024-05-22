# 감소하는 수

import sys

input = sys.stdin.readline

n = int(input())

dp = list([0 for _ in range(10)] for _ in range(11))


dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

last_dp = 9

end = False
ans_depth = 0
ans_key = 0

# n번째 감소하는 수의 번째를 계산하는 테이블
if n > 9:
    for i in range(2, 11):
        for j in range(i - 1, 10):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            last_dp += dp[i][j]
            if n <= last_dp:
                end = True  # 찾으면 끝낸다
                ans_depth = i  # 백트래킹에서 사용할 depth
                ans_key = j  # 백트래킹에서 사용할 가장 큰 자릿 수
                cnt = last_dp - n  # 해당 칸에서의 몇번째로 큰 숫자인지 확인
                break
        if end == True:
            break

# print(dp)
# print(last_dp)
in_count = -1


def dfs(depth, start_num, ans: str):
    global in_count
    if depth == ans_depth:  # 목적지의 뎁스와 맞고
        in_count += 1
        if cnt == in_count:  # 찾는 번째의 숫자
            return ans
        else:
            ans = ans[:-1]  # 아니면 맨 끝 수를 지운다
    else:
        for i in range(start_num - 1, -1, -1):  # 큰 수에서 하나씩 줄여간다
            result = dfs(depth + 1, i, ans + str(i))
            if result is not None:
                return result


if end == True:
    print(dfs(1, ans_key, str(ans_key)))  # 뎁스, 시작 숫자, 결과 문자열의 시작 부분
else:
    if n <= 9:
        print(n)
    else:
        print(-1)
