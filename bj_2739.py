# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

import sys


def gugu(num):
    for i in range(1, 10):
        result = num * i
        print(f"{num} * {i} = {result}")


if __name__ == "__main__":
    gugu(int(sys.stdin.readline().strip()))
