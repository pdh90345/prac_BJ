# 출석 체크

import sys

n, k, q, m = map(int, sys.stdin.readline().split())
k_arr = list(map(int, sys.stdin.readline().split()))

q_arr = list(map(int, sys.stdin.readline().split()))


chk = [0] * (n + 3)  # n+3까지
chk[0] = 1
chk[1] = 1
chk[2] = 1

for i in range(len(k_arr)):
    chk[k_arr[i]] = -1

for person in q_arr:
    for i in range(person, n + 3, person):
        if chk[person] == -1:
            break
        elif chk[i] != -1:
            chk[i] = 1

result = [0] * (n + 3)
count = 0
for i in range(3, n + 3):
    if chk[i] != 1:
        count += 1
    result[i] = count
# print(chk)
# print(result)
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(result[e] - result[s - 1])
