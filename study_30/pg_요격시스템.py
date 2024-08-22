def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[1], x[0]))
    answer, end = 0, 0
    for s, e in targets:
        if end <= s:  # s 보다 현재 end가 작거나 같을때는 요격 불가하므로
            answer += 1  # 요격 추가
            end = e  # 해당 미사일의 e를 end로 바꾼다

    return answer
