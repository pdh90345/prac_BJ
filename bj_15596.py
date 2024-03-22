# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
# 작성해야 하는 함수는 다음과 같다.
import sys


def solve(a: list) -> int:
    return sum(a)


if __name__ == "__main__":
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(numbers))
