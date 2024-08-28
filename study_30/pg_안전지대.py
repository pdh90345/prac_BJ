def solution(board):
    answer = len(board) * len(board[0])

    # 왼쪽위 부터 오른쪽 아래까지 차례대로 확인
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def findSave(x, y):
        answer = 1
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    answer += 1
        return answer

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                answer -= findSave(i, j)

    return answer


# def solution(board):
#     answer = 0

#     # 왼쪽위 부터 오른쪽 아래까지 차례대로 확인
#     dx = [-1, -1, -1, 0, 0, 1, 1, 1]
#     dy = [-1, 0, 1, -1, 1, -1, 0, 1]

#     def findSave(x, y):
#         for i in range(len(dx)):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
#                 if board[nx][ny] == 0:
#                     board[nx][ny] = 2

#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 1:
#                 findSave(i, j)

#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 0:
#                 answer += 1

#     return answer
