# 회의실 배정
# 빨리 끝나는 순
import sys

n = int(input())

meeting = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append([s, e])
meeting.sort(key=lambda x: (x[1], x[0]))

# print(meeting)

cnt = 1
end = meeting[0][1]
for i in range(1, n):
    if end <= meeting[i][0]:
        end = meeting[i][1]
        cnt += 1
print(cnt)

# result = 0
# for i in range(n):
#     cnt = 1
#     if n - i < result:
#         break

#     end = meeting[i][1]
#     for j in range(i + 1, n):
#         n_start = meeting[j][0]
#         if end <= n_start:
#             end = meeting[j][1]
#             cnt += 1
#     result = max(result, cnt)
# print(result)
