# 흙길 보수하기

import sys

input = sys.stdin.readline

n, l = map(int, input().split())

arr = []

for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))


def calBoard(holeStart, holeEnd, boardLength):  # 보드 개수 계산
    totalLength = (
        holeEnd - holeStart + boardLength - 1
    )  # 웅덩이 길이에 보드길이 - 1을 더해서 올림이 되게 한다
    requiredBoard = totalLength // boardLength
    return requiredBoard


arr.sort()
boardEnd = 0
result = 0
for s, e in arr:
    if boardEnd > s and boardEnd > e - 1:  # 보드가 웅덩이의 시작과 끝보다 클때는 스킵
        continue
    elif boardEnd > s:  # 보드가 웅덩이의 시작보다 크면 시작지점을 보드의 끝으로 바꾼다
        s = boardEnd
    cntBoard = calBoard(s, e, l)
    boardEnd = s + l * cntBoard
    result += cntBoard

print(result)
