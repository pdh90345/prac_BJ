# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

import sys

n = int(input())
strList = []
for _ in range(n):
    strList.append(sys.stdin.readline().strip())

setList = set(strList)

sortList = sorted(setList, key=lambda x: (len(x), x))


for word in sortList:
    print(word)
