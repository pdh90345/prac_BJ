# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

import sys


list9 = []
result = 0

for _ in range(9):
    value = int(sys.stdin.readline().strip())
    list9.append(value)
    result = result + value

for i in range(8):
    for j in range(i + 1, 9):
        if result - (list9[i] + list9[j]) == 100:
            del list9[j]
            del list9[i]
            break
    if len(list9) == 7:
        break


list9.sort()

for person in list9:
    print(person)
