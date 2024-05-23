# 조합 0의 개수

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 12!를 예시로
# 12 / 2 = 6 -> 12!에 있는 수에서 2로 나눌때 나눠지는 수의 개수 -> 6개
# 6 / 2 = 3 -> 12!에서 2로 나눈 나머지 값에서 또 2로 나눌때 나눠지는 개수 -> 3개
# 3 / 2 = 1 -> 또 나눠지는 개수 -> 1개


def f_power_count(x, f):
    cnt = 0
    while x >= f:
        x //= f
        cnt += x

    return cnt


cnt_two = f_power_count(n, 2) - f_power_count(n - m, 2) - f_power_count(m, 2)
cnt_five = f_power_count(n, 5) - f_power_count(n - m, 5) - f_power_count(m, 5)

print(min(cnt_two, cnt_five))  # 2, 5 중 최소값이 10을 만들수 있는 개수
