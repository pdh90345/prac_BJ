def solution(left, right):
    answer = 0

    square = []
    for i in range(1, 1000):
        square.append(i * i)

    for i in range(left, right + 1):
        if i in square:
            answer -= i
        else:
            answer += i

    return answer
