# 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축

# 첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다.
# 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.
# import sys

# n = int(input())
# tree = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]


# def check(tree: list):
#     return all(element == tree[0][0] for row in tree for element in row)


# def div(tree: list, rf: int, rl: int, cf: int, cl: int):
#     midr = (rf + rl) // 2
#     midc = (cf + cl) // 2

#     part_tree = [row[cf : cl + 1] for row in tree[rf : rl + 1]]
#     if check(part_tree):
#         print(part_tree)
#     else:
#         div(tree, rf, midr, cf, midc)
#         div(tree, rf, midr, midc + 1, cl)
#         div(tree, midr + 1, rl, cf, midc)
#         div(tree, midr + 1, rl, midc + 1, cl)


# div(tree, 0, n - 1, 0, n - 1)

import sys

n = int(input())
tree = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]


def check(tree: list):
    # 주어진 영역의 모든 원소가 같은지 확인
    return all(element == tree[0][0] for row in tree for element in row)


def div(tree: list, rf: int, rl: int, cf: int, cl: int):
    # 현재 영역을 추출
    part_tree = [row[cf : cl + 1] for row in tree[rf : rl + 1]]
    # 현재 영역의 모든 값이 같다면 해당 값을 출력
    if check(part_tree):
        print(part_tree[0][0], end="")
    else:
        # 값이 다르면 4분할하여 각 분할 영역에 대해 재귀적으로 div 함수 호출
        print("(", end="")
        midr = (rf + rl) // 2
        midc = (cf + cl) // 2
        div(tree, rf, midr, cf, midc)
        div(tree, rf, midr, midc + 1, cl)
        div(tree, midr + 1, rl, cf, midc)
        div(tree, midr + 1, rl, midc + 1, cl)
        print(")", end="")


div(tree, 0, n - 1, 0, n - 1)
