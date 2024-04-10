# 잃어버린 괄호

exp = list(input())
pm = [0] * 2
chk = ["+"]
temp = 0

for i in range(len(exp)):
    if exp[i] == "+":
        if chk[0] == "+":
            pm[0] += temp
            temp = 0
        else:
            pm[1] += temp
            temp = 0
        continue
    elif exp[i] == "-":
        if chk[0] == "+":
            pm[0] += temp
            temp = 0
            chk[0] = "-"
        else:
            pm[1] += temp
            temp = 0
        continue
    temp = temp * 10 + int(exp[i])

    if i == len(exp) - 1:
        if chk[0] == "-":
            pm[1] += temp
        else:
            pm[0] += temp


print(pm[0] - pm[1])
