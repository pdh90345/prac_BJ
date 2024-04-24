# 에디터
# 다시 풀어보기
import sys

s1 = list(map(str, sys.stdin.readline().strip()))
s2 = []
n = int(input())

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())
    if len(command) == 1:
        if command[0] == "L":
            if len(s1) > 0:
                s2.append(s1.pop())
        elif command[0] == "D":
            if len(s2) > 0:
                s1.append(s2.pop())
        elif command[0] == "B":
            if s1:
                s1.pop()
    else:
        s1.append(command[1])

s1.extend(reversed(s2))
print("".join(s1))


# class ListNode:
#     def __init__(self, value, prev, next):
#         self.value = value
#         self.prev = prev
#         self.next = next


# head = ListNode(0, None, None)
# cur = head

# arr = list(sys.stdin.readline().strip())
# n = int(input())

# for i in range(len(arr)):
#     newNode = ListNode(arr[i], None, None)
#     cur.next = newNode
#     newNode.prev = cur
#     cur = newNode

# for _ in range(n):
#     command = list(sys.stdin.readline().split())
#     if len(command) == 1:
#         if command[0] == "L":
#             if cur.value != 0:
#                 cur = cur.prev
#         elif command[0] == "D":
#             if cur.next != None:
#                 cur = cur.next
#         elif command[0] == "B":
#             if cur.value != 0:
#                 cur = cur.prev
#                 if cur.next.next:
#                     cur.next = cur.next.next
#                     cur.next.prev = cur
#                 else:
#                     cur.next = None
#     else:
#         newNode = ListNode(command[1], None, None)
#         if cur.next:
#             newNode.next = cur.next
#             cur.next.prev = newNode
#         cur.next = newNode
#         newNode.prev = cur
#         cur = newNode

# cur = head.next
# while cur != None:
#     print(cur.value, end="")
#     cur = cur.next
