# 백준 10828_스택
# implementation

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    c = input().split()
    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop()) # pop한 것 바로 출력 가능
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1]) # 리스트[-1] : 뒤에서 첫번째 데이터 