# 트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 10^6보다 작은 양의 정수이다.
# 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.
# 입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.

# 다시 풀어보기

import sys

sys.setrecursionlimit(10**9)

pre = []

while True:
    try:
        pre.append(int(sys.stdin.readline().strip()))
    except:
        break


def pre_to_pro(start: int, end: int):
    if start > end:
        return
    right_start = end + 1  # 모두 루트보다 작을경우 end값 만드는 역할
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            right_start = i
            break
    pre_to_pro(start + 1, right_start - 1)  # 왼쪽 서브트리
    pre_to_pro(right_start, end)  # 오른쪽 서브트리
    print(pre[start])  # 루트


pre_to_pro(0, len(pre) - 1)
