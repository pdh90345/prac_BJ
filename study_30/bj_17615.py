# 볼 모으기

import sys

input = sys.stdin.readline

n = int(input())


balls = input().strip()
answer = int(1e8)

# 1. R을 모두 왼쪽으로 이동
balls_1 = balls.lstrip("R")
answer = min(answer, balls_1.count("R"))

# 2. B를 모두 왼쪽으로 이동
balls_2 = balls.lstrip("B")
answer = min(answer, balls_2.count("B"))

# 3. R을 모두 오른쪽으로 이동
balls_3 = balls.rstrip("R")
answer = min(answer, balls_3.count("R"))

# 4. B를 모두 오른쪽으로 이동
balls_4 = balls.rstrip("B")
answer = min(answer, balls_4.count("B"))

print(answer)

# balls = list(map(str, input().strip()))

# front = balls[0]
# end = balls[n - 1]

# all_b = 0
# all_r = 0
# for i in range(n):
#     if balls[i] == "B":
#         all_b += 1
#     else:
#         all_r += 1

# front_count = 1
# for i in range(1, n):
#     if front == balls[i]:
#         front_count += 1
#     else:
#         break
# end_count = 1
# for i in range(n - 2, -1, -1):
#     if end == balls[i]:
#         end_count += 1
#     else:
#         break

# if front == end:
#     if front_count >= end_count:
#         if balls[0] == "R":
#             red_count = all_r - front_count
#             if red_count < all_b:
#                 print(red_count)
#             else:
#                 print(all_b)
#         else:
#             blue_count = all_b - front_count
#             if blue_count < all_r:
#                 print(blue_count)
#             else:
#                 print(all_r)
#     else:
#         if balls[n - 1] == "R":
#             red_count = all_r - end_count
#             if red_count < all_b:
#                 print(red_count)
#             else:
#                 print(all_b)
#         else:
#             blue_count = all_b - end_count
#             if blue_count < all_r:
#                 print(blue_count)
#             else:
#                 print(all_r)
# else:
#     if front == "R":
#         result1 = all_r - front_count
#     else:
#         result1 = all_b - front_count
#     if end == "R":
#         result2 = all_r - end_count
#     else:
#         result2 = all_b - end_count
#     print(min(result1, result2))
