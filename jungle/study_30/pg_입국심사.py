def solution(n, times):
    answer = 0

    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        chk = 0
        for time in times:  # 한 심사대가 몇명을 확인 가능한지
            chk += mid // time
            if chk >= n:  # chk가 n을 넘어가면 불필요한 반복 종료
                break

        if chk >= n:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer
