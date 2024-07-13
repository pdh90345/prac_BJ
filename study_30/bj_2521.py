# 예산

import sys

input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))

m = int(input().strip())


def findResult(l, r):
    while l <= r:
        mid = (l + r) // 2
        check = 0
        for budget in budgets:
            if (
                budget < mid
            ):  # 예산들 중 mid값보다 작은 예산만 골라서 mid - budget 해준다.
                check += mid - budget

        checkBudget = mid * len(budgets) - check  # 최대 가능 예산 확인

        if checkBudget == m:
            return mid
        elif checkBudget > m:
            r = mid - 1
        else:
            l = mid + 1
    return r


result = findResult(1, max(budgets))

print(result)
