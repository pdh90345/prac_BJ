# 단어 수학

import sys, heapq

input = sys.stdin.readline

n = int(input())
str_list = []
for i in range(n):
    str_alpa = input().strip()
    reverse_name = ""
    for c in str_alpa:
        reverse_name = c + reverse_name
    str_list.append(reverse_name)

alpa_dict = {chr(i): -1 for i in range(65, 91)}  # A-Z
count_dict = {chr(i): 0 for i in range(65, 91)}  # A-Z
# alpa_dict = {
#     "A": -1,
#     "B": -1,
#     "C": -1,
#     "D": -1,
#     "E": -1,
#     "F": -1,
#     "G": -1,
#     "H": -1,
#     "I": -1,
#     "J": -1,
#     "K": -1,
#     "L": -1,
#     "N": -1,
#     "M": -1,
#     "O": -1,
#     "P": -1,
#     "Q": -1,
#     "R": -1,
#     "S": -1,
#     "T": -1,
#     "U": -1,
#     "V": -1,
#     "W": -1,
#     "X": -1,
#     "Y": -1,
#     "Z": -1,
# }
# count_dict = {
#     "A": -1,
#     "B": -1,
#     "C": -1,
#     "D": -1,
#     "E": -1,
#     "F": -1,
#     "G": -1,
#     "H": -1,
#     "I": -1,
#     "J": -1,
#     "K": -1,
#     "L": -1,
#     "N": -1,
#     "M": -1,
#     "O": -1,
#     "P": -1,
#     "Q": -1,
#     "R": -1,
#     "S": -1,
#     "T": -1,
#     "U": -1,
#     "V": -1,
#     "W": -1,
#     "X": -1,
#     "Y": -1,
#     "Z": -1,
# }

# 각 알파벳 빈도수 계산
for word in str_list:
    for idx, char in enumerate(word):
        count_dict[char] += 10**idx

# for word in str_list:
#     length = len(word)
#     for idx in range(length):
#         char = word[idx]
#         count_dict[char] += 10 ** idx

hq = []
num = 9

# 각 알파벳의 빈도수를 기준으로 힙에 추가
for char, freq in count_dict.items():
    if freq > 0:
        heapq.heappush(hq, (-freq, char))  # 빈도수를 음수로 하여 최대 힙처럼 사용

# for char in count_dict:
#     freq = count_dict[char]
#     if freq > 0:
#         heapq.heappush(hq, (-freq, char))

# 힙에서 꺼내서 알파벳에 숫자 할당
while hq:
    freq, alpa = heapq.heappop(hq)
    alpa_dict[alpa] = num
    num -= 1

result = 0
for line in str_list:
    for j in range(len(line) - 1, -1, -1):
        result += alpa_dict[line[j]] * (10**j)

print(result)
