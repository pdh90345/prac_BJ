# 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

import sys

n, m = list(map(int, input().split()))  # 나무개수, 필요한 나무 길이

woods = list(map(int, sys.stdin.readline().split()))  # 나무 길이 리스트
woods.sort()


# 10 15 17 20
def cut():
    first = 0
    last = woods[len(woods) - 1]
    result = 0
    while first <= last:
        h = (first + last) // 2
        rs = 0
        for wood in woods:
            if wood - h > 0:
                rs += wood - h  # 자르고 가져갈수 있는 나무 -> 최대한 m에 가깝도록
        if rs == m:
            result = h
            return result
        if rs > m:
            result = h
            first = h + 1
        elif rs < m:
            last = h - 1
    return result


print(cut())
