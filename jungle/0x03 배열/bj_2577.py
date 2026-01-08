# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

result = a * b * c

arr = [0] * 10

while result != 0:
    arr[result % 10] += 1
    result //= 10

for num in arr:
    print(num, end=" ")
