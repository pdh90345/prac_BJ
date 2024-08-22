# tickets = [
#     ["ICN", "BOO"],
#     ["ICN", "COO"],
#     ["COO", "DOO"],
#     ["DOO", "COO"],
#     ["BOO", "DOO"],
#     ["DOO", "BOO"],
#     ["BOO", "ICN"],
#     ["COO", "BOO"],
# ]
tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]


def solution(tickets):
    answer = []
    for i in range(len(tickets)):
        arr = []
        chk = [0] * len(tickets)
        if tickets[i][0] == "ICN":  # 시작은 ICN부터
            chk[i] = 1
            arr.extend(
                [tickets[i][0], tickets[i][1]]
            )  # ICN과 연결된 e도 함께 추가해준다
            dfs(tickets, chk, arr, answer)
    answer.sort()  # 알파벳 순 정렬
    # print(answer)
    return answer[0]


def dfs(tickets, chk, arr, answer):
    if len(arr) == len(tickets) + 1:
        answer.append(arr[:])  # return이 없기 때문에 얕은 복사를 해야지 영향이 없다.
    else:
        for i in range(len(tickets)):
            s, e = tickets[i][0], tickets[i][1]
            if arr[-1] == s and chk[i] == 0:
                # print(arr)
                # print(s)
                arr.append(e)
                chk[i] = 1
                dfs(tickets, chk, arr, answer)
                arr.pop()  # 중복 티켓이 있을 수 있으므로 다시 지워줘야 한다.
                chk[i] = 0


print(solution(tickets))
