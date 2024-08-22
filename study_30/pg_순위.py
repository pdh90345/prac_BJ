# 순위
# 다시 풀기


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]


from collections import defaultdict, deque


def solution(n, results):
    answer = 0

    def bfs(graph, start):
        queue = deque([start])
        visited = set([start])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    graph[start].append(neighbor)
                    queue.append(neighbor)
                    visited.add(neighbor)

    # 승자와 패자를 기록하는 딕셔너리
    wins = defaultdict(list)
    losses = defaultdict(list)

    # 결과 입력 처리
    for winner, loser in results:
        wins[winner].append(loser)
        losses[loser].append(winner)

    # 각 선수에 대해 BFS를 수행하여 모든 가능한 승리 및 패배를 계산
    for i in range(1, n + 1):
        bfs(wins, i)
        bfs(losses, i)

    # 순위를 확정할 수 있는 선수의 수를 계산
    for i in range(1, n + 1):
        if len(set(wins[i])) + len(set(losses[i])) == n - 1:
            answer += 1
    return answer


# def solution(n, results):
#     answer = 0
#     dictw = defaultdict(list)
#     dictl = defaultdict(list)

#     for game in results:
#         w, l = game[0], game[1]
#         dictw[w].append(l)
#         dictl[l].append(w)

#     for i in range(1, n + 1):
#         d = deque()
#         chk = set()
#         d.append(i)
#         chk.add(i)
#         bfs(dictw, d, chk, i)
#         d = deque()
#         chk = set()
#         d.append(i)
#         chk.add(i)
#         bfs(dictl, d, chk, i)

#     for i in range(1, n + 1):
#         if len(set(dictw[i])) + len(set(dictl[i])) == n - 1:
#             answer += 1

#     return answer


# def bfs(dicts, d, chk, i):
#     while d:
#         x = d.popleft()
#         for j in dicts[x]:
#             if j not in chk:
#                 dicts[i].append(j)
#                 d.append(j)
#                 chk.add(j)


print(solution(n, results))
