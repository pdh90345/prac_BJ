# 균형 잡힌 세상

import sys

stack = []

while True:
    chkbreak = False
    str_arr = list(map(str, sys.stdin.readline().strip("\n")))
    if len(str_arr) == 1:
        break
    for i in range(len(str_arr) - 1):
        if str_arr[i] == "[" or str_arr[i] == "(":
            stack.append(str_arr[i])
            continue
        elif str_arr[i] == "]":
            if not stack:
                chkbreak = True
                break
            else:
                if stack.pop() == "[":
                    continue
                else:
                    chkbreak = True
                    break
        elif str_arr[i] == ")":
            if not stack:
                chkbreak = True
                break
            else:
                if stack.pop() == "(":
                    continue
                else:
                    chkbreak = True
                    break
    if stack:
        chkbreak = True
    if not chkbreak:
        print("yes")
        stack = []
    else:
        print("no")
        stack = []
