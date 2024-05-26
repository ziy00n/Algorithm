# 백준 7562_나이트의 이동
# BFS

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

dy = [-2,-1,-2,-1,1,2,2,1]
dx = [-1,-2,1,2,-2,-1,1,2]

for _ in range(T):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    visited = [[0] * l for _ in range(l)]
    
    y1, x1 = map(int, input().split())
    a, b = map(int, input().split())
    
    q = deque()
    def bfs():
        q.append([y1, x1])
        visited[y1][x1] = 1
        
        while q:
            y, x = q.popleft()
            
            if y == a and x == b:
                return visited[y][x]-1
            
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < l and 0 <= nx < l:
                    if visited[ny][nx] == 0:
                        q.append([ny, nx])
                        visited[ny][nx] = visited[y][x] + 1
    
    answer = bfs()
    print(answer)