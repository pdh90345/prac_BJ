# 스타트와 링크

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


# def split_comb():
#     board_index = [i for i in range(n)]  # 조합을 만들기위한 보드 인덱스
#     all_comb = list(combinations(board_index, n // 2)) # 길이의 반만큼의 조합을 만든다
#     seen = set() # 등장했던 조합인지 확인
#     result = []

#     for combo in all_comb:
#         remaining_list = [] # 뽑히지 않은 수들 (반대팀의 조합)
#         for x in board_index:
#             if x not in combo:
#                 remaining_list.append(x)
#         remaining = tuple(remaining_list)

#         if combo not in seen and remaining not in seen:
#             result.append((combo, remaining))
#             seen.add(combo) # 등장한 조합 추가
#             seen.add(remaining) # 반대팀 조합도 추가

#     return result


def split_comb():  # 튜플과 집합
    board_index = set(range(n))
    seen = set()
    result = []
    all_comb = combinations(board_index, n // 2)
    for comb in all_comb:
        Ateam = comb
        comb = set(comb)
        Bteam = tuple(board_index - comb)

        if Ateam not in seen and Bteam not in seen:
            result.append((Ateam, Bteam))
            seen.add(Ateam)
            seen.add(Bteam)
    return result


ans = sys.maxsize
teams = split_comb()

for check_team in teams:
    team_a = check_team[0]
    team_b = check_team[1]
    a_count = 0
    for i in team_a:
        for j in team_a:
            if i != j:
                a_count += board[i][j]
    b_count = 0
    for i in team_b:
        for j in team_b:
            if i != j:
                b_count += board[i][j]
    ans = min(ans, abs(a_count - b_count))
    if ans == 0:
        break

print(ans)
