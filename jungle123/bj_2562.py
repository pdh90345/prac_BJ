# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
import sys

if __name__ == "__main__":

    maximum = 1
    for i in range(9):
        num = int(sys.stdin.readline().strip())
        if num > maximum:
            maximum = num
            count = i

    print(maximum)
    print(int(count + 1))
