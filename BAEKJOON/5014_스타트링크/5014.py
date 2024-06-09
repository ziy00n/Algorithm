# 백준 5014_스타트링크
# BFS

import sys
input = sys.stdin.readline
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [0] * (F+1) # 방문처리 & 버튼 누른 횟수

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1 # 현재 강호 위치 방문처리(버튼누른 횟수는 -1해야함)
    
    while q:
        x = q.popleft()
        if x == G:
            return visited[x]-1
        
        for i in [x+U, x-D]:
            if 1 <= i <= F and visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1
                
    return 'use the stairs'

print(bfs(S))