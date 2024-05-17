# 걸그룹 마스터 준석이

import sys

input = sys.stdin.readline

t, q = map(int, input().split())
team_dic = {}
for _ in range(t):
    t_name = input().strip()
    num = int(input().strip())
    idol = []
    for i in range(num):
        idol.append(input().strip())
    idol.sort()
    team_dic[t_name] = idol

for _ in range(q):
    question = input().strip()
    q_type = int(input().strip())

    if q_type:  # 1일 때는 팀출력
        for key, value in team_dic.items():
            if question in value:
                print(key)
    else:
        for key, value in team_dic.items():
            if question in key:
                for i in range(len(value)):
                    print(value[i])

print(team_dic.items())
