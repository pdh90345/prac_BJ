# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

import sys

cnt = 0
isused1 = [False] * 29  # 열
isused2 = [False] * 29  # /
isused3 = [False] * 29  # \


def func(cur: int):
    global cnt
    global n
    if cur == n:
        cnt += 1
        return
    for i in range(n):
        if isused1[i] or isused2[cur + i] or isused3[cur - i + n - 1]:
            continue
        isused1[i] = True
        isused2[cur + i] = True
        isused3[cur - i + n - 1] = True
        func(cur + 1)  # 백트래킹 후 경로 초기화
        isused1[i] = False
        isused2[cur + i] = False
        isused3[cur - i + n - 1] = False


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    func(0)
    print(cnt)
