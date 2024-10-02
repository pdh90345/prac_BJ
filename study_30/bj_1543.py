# 문서 검색

import sys

input = sys.stdin.readline

n = list(map(str, input().strip()))
find = list(map(str, input().strip()))

ans = 0
index = 0

while len(n) - len(find) >= index:
    fi = 0
    while fi != len(find):
        if n[index + fi] == find[fi]:
            fi += 1
        else:
            break
    if fi == len(find):
        ans += 1
        index += len(find)  # 맞으면 타겟단어 크기만큼 뒤에서 시작
    else:
        index += 1

print(ans)
