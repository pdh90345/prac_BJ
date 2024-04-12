# LCS
# 다시

import sys

X = list(map(str, sys.stdin.readline().strip()))
X.insert(0, 0)
Y = list(map(str, sys.stdin.readline().strip()))
Y.insert(0, 0)

dp = [[0 for _ in range(len(Y))] for _ in range(len(X))]

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        if X[i] == Y[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(X) - 1][len(Y) - 1])
