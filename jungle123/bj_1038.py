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

if n > 9:
    for i in range(2, 11):
        for j in range(i - 1, 10):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            last_dp += dp[i][j]
            if n <= last_dp:
                end = True
                ans_depth = i
                ans_key = j
                cnt = last_dp - n
                break
        if end == True:
            break

# print(dp)
# print(last_dp)
in_count = -1


def dfs(depth, start_num, ans: str):
    global in_count
    if depth == ans_depth:
        in_count += 1
        if cnt == in_count:
            return ans
        else:
            ans = ans[:-1]
    else:
        for i in range(start_num - 1, -1, -1):
            result = dfs(depth + 1, i, ans + str(i))
            if result is not None:
                return result


if end == True:
    print(dfs(1, ans_key, str(ans_key)))
else:
    if n <= 9:
        print(n)
    else:
        print(-1)
