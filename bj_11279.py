# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

# 입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

import heapq, sys

n = int(input())
heap = []

for i in range(n):
    x = int(sys.stdin.readline().strip())
    if not x:
        if not heap:
            print(0)
        else:
            rs = heapq.heappop(heap)
            print(-rs)
    else:
        heapq.heappush(heap, -x)
