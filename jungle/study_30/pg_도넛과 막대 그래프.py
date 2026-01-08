def solution(edges):
    answer = []
    maxNode = 0  # 노드 최대 값
    for nodes in edges:
        for i in nodes:
            maxNode = max(i, maxNode)
    degree = {i: [0, 0] for i in range(1, maxNode + 1)}  # (in, out)

    for outDegree, inDegree in edges:
        degree[outDegree][1] += 1  # 나가는 노드에 1 추가
        degree[inDegree][0] += 1  # 들어오는 노드에 1 추가

    start, donut, stick, eight = 0, 0, 0, 0

    for node in degree:
        inD = degree[node][0]
        outD = degree[node][1]

        if inD == 0 and outD >= 2:
            startNum = node  # 생성 노드
            start = outD  # 그래프의 개수는 생성 노드의 outD
        elif inD >= 2 and outD == 2:
            eight += 1
        elif inD >= 1 and outD == 0:
            stick += 1

    donut = start - (eight + stick)

    answer.extend([startNum, donut, stick, eight])
    return answer
