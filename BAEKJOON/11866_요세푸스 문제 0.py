# 백준 11866_요세푸스 문제 0
# implementation

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

queue = deque(range(1, N+1)) # 1 ~ N 까지 덱에 담기
seq = []

for _ in range(N):
    for _ in range(K-1): # k-1 번 (k번째 수의 앞 숫자들)
        queue.append(queue.popleft()) # 큐의 맨 앞 숫자를 삭제 후 맨 뒤에 넣기
    seq.append(queue.popleft())

# print('<', end='')
# for i in range(N-1):
#     print(seq[i], end=', ')
# print(seq[-1], end='')
# print('>')
print('<',', '.join(list(map(str, seq))), '>', sep="")