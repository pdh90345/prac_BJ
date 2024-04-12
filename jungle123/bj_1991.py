# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
import sys
from collections import deque


n = int(input())
bt = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]


node_to_index = {}
for i in range(len(bt)):
    node = bt[i]
    node_name = node[0]
    node_to_index[node_name] = i  # 이름이 키


def Pre(index: int):
    node = bt[index][0]
    print(node, end="")
    if bt[index][1] != ".":
        Pre(node_to_index[bt[index][1]])
    if bt[index][2] != ".":
        Pre(node_to_index[bt[index][2]])


def In(index: int):
    node = bt[index][0]
    if bt[index][1] != ".":
        In(node_to_index[bt[index][1]])
    print(node, end="")
    if bt[index][2] != ".":
        In(node_to_index[bt[index][2]])


def Pro(index: int):
    node = bt[index][0]
    if bt[index][1] != ".":
        Pro(node_to_index[bt[index][1]])
    if bt[index][2] != ".":
        Pro(node_to_index[bt[index][2]])
    print(node, end="")


Pre(0)
print()
In(0)
print()
Pro(0)
