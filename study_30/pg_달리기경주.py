def solution(players, callings):
    answer = []
    rank = {}
    for v, k in enumerate(players):
        rank[k] = v

    for call in callings:
        idx = rank[call]

        players[idx], players[idx - 1] = players[idx - 1], players[idx]  # 사람 바꾸고

        rank[players[idx]] = idx  # 랭킹을 바꾼다 (시간 줄이기 위해 딕셔너리)
        rank[players[idx - 1]] = idx - 1
    answer = players

    return answer
