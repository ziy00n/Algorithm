# 백준 10866_덱
# implementation

import sys
input = sys.stdin.readline

N = int(input())

deque = []
for _ in range(N):
    c = input().split()

    if c[0] == 'push_front':
        deque.insert(0, c[1]) # insert(index, element) : 해당 인덱스에 요소 추가 
    elif c[0] == 'push_back':
        deque.append(c[1])
    elif c[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0)) # pop() : 맨 뒤값 삭제, 인덱스 지정하면 그 위치 값 삭제
    elif c[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif c[0] == 'size':
        print(len(deque))
    elif c[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif c[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])