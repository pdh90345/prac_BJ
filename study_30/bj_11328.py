# Strfry

import sys

n = int(input())

string_list = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
chk_list = [0] * n
for i in range(n):
    string_a = string_list[i][0]
    string_b = string_list[i][1]

    sort_a = sorted(string_a)
    sort_b = sorted(string_b)

    chk = 0

    for j in range(len(sort_a)):
        if sort_a[j] == sort_b[j]:
            chk += 1
        else:
            break

    if chk == len(string_a):
        chk_list[i] = 1
for check in chk_list:
    if check:
        print("Possible")
    else:
        print("Impossible")


# for _ in range(int(input())):
#   a,b=map(list,input().split())
#   a.sort()
#   b.sort()
#   if a==b:
#     print('Possible')
#   else:
#     print('Impossible')
