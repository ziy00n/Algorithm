# 백준 10773_제로
# implementation

import sys
input = sys.stdin.readline
k = int(input())

stack = []

for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

sum = 0
for i in stack:
    sum += i

print(sum)