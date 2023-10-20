# 백준 2346_풍선 터뜨리기
# Data Structure

from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split()))) 
ans = []

for i in range(n):
    idx, tmp = q.popleft()
    print(idx +1, end =' ')
    if tmp > 0:
        q.rotate(-(tmp -1))
    else:
        q.rotate(-tmp)