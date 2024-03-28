# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
import sys, itertools

n, s = map(int, input().split())

numList = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0
for i in range(1, n + 1):
    combi = list(itertools.combinations(numList, i))
    for j in range(len(combi)):
        if sum(combi[j]) == s:
            cnt += 1

print(cnt)
