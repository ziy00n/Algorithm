# 백준 10845_큐
# 자료구조


# 스택 이용해서 큐 구현
import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])