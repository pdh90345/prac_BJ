# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# base conditon : 0! = 1, 1! = 1
# 1...k k+1 ... n

import sys


def fact(n: int) -> int:
    if n <= 1:
        return 1
    return n * fact(n - 1)


if __name__ == "__main__":
    print(fact(int(sys.stdin.readline().strip())))
