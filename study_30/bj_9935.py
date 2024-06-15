# 문자열 폭발

import sys

input = sys.stdin.readline

arr = list(map(str, input().strip()))
bomb = list(map(str, input().strip()))


stack = []
# 시간 단축
for i in arr:
    stack.append(i)
    if stack[-len(bomb) :] == bomb:  # 여러 요소를 한번에 확인 가능
        for j in range(len(bomb)):
            stack.pop()

if stack:
    print(*stack, sep="")
else:
    print("FRULA")


# while arr:
#     arr_top = arr.pop()
#     stack.append(arr_top)
#     if len(stack) >= len(bomb):
#         cnt = 0
#         for i in range(len(bomb)):
#             if stack[-1 - i] == bomb[i]:
#                 cnt += 1
#             else:
#                 break
#         if cnt == len(bomb):
#             for i in range(cnt):
#                 stack.pop()

# if stack:
#     result = stack[::-1]
#     print(*result, sep="")
# else:
#     print("FRULA")


# 시간 초과
# loop_cnt = 100000
# for i in bomb:
#     cnt = 0
#     for j in arr:
#         if i == j:
#             cnt += 1
#     loop_cnt = min(loop_cnt, cnt)


# for i in range(loop_cnt):
#     chk = False
#     for j in range(len(arr)):
#         if arr[j] == bomb[0]:
#             cnt = 1
#             for k in range(1, len(bomb)):
#                 if j + k <= len(arr) - 1 and arr[j + k] == bomb[k]:
#                     cnt += 1
#                 if cnt == len(bomb):
#                     arr = arr[:j] + arr[j + k + 1 :]
#                     chk = True
#                     break
#         if chk == True:
#             break

# if len(arr) == 0:
#     print("FRULA")
# else:
#     print(*arr)
