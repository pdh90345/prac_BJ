from collections import defaultdict


def solution(weights):
    answer = 0

    dd = defaultdict(int)
    ratios = [(1, 2), (2, 3), (3, 4)]

    for weight in weights:
        dd[weight] += 1

    for weight, people in dd.items():
        answer += people * (people - 1) // 2  # nC2
        for a, b in ratios:
            # RuntimeError: dictionary changed size during iteration
            if (
                weight * a / b in dd.keys()
            ):  # defaultdict는 자동으로 키가 추가 되므로 조건문을 달아서 새로운 키가 추가되지 않게 해야한다.
                answer += people * dd[weight * a / b]

    return answer


# from collections import Counter

# def solution(weights):
#     answer = 0

#     people_counter = Counter(weights)
#     ratios = [(1, 2), (2, 3), (3, 4)]

#     for weight, people in people_counter.items():
#         answer += people * (people - 1) // 2
#         for a, b in ratios:
#             scaled_weight = weight * a / b # 카운터는 노 상관
#             answer += people * people_counter[scaled_weight]

#     return answer
