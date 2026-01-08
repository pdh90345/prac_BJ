numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "right"


def solution(numbers, hand):
    answer = ""
    L = 10
    R = 12
    leftNum = [1, 4, 7]
    rightNum = [3, 6, 9]

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]  # 키패드 위치

    def calcHand(left: int, right: int, number: int, hand):
        touchHand = ""
        if number == 0:
            number = 11
        if left == 0:
            left = 11
        if right == 0:
            right = 11

        def findPos(num):  # 좌표 확인
            for i, row in enumerate(matrix):
                if num in row:
                    return i, row.index(num)

        tempLx, tempLy = findPos(left)  # type: ignore
        tempRx, tempRy = findPos(right)  # type: ignore
        tempNx, tempNy = findPos(number)  # type: ignore

        # 길이가 같으면 주 손, 아니면 작은 길이의 손
        if abs(tempLx - tempNx) + abs(tempLy - tempNy) == abs(tempRx - tempNx) + abs(
            tempRy - tempNy
        ):
            if hand == "right":
                touchHand = "R"
            else:
                touchHand = "L"
        elif abs(tempLx - tempNx) + abs(tempLy - tempNy) < abs(tempRx - tempNx) + abs(
            tempRy - tempNy
        ):
            touchHand = "L"
        else:
            touchHand = "R"

        return touchHand, number

    for number in numbers:
        if number in leftNum:
            L = number
            answer += "L"
        elif number in rightNum:
            R = number
            answer += "R"
        else:
            touchHand, number = calcHand(L, R, number, hand)
            if touchHand == "L":
                L = number
            else:
                R = number
            answer += touchHand

    return answer


print(solution(numbers, hand))
