# 백준 2468_안전 영역
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

h = 0
for row in graph:
    h = max(max(row), h)


dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y, x, k):
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<= ny < n and 0 <= nx < n:
                if graph[ny][nx] > k and not visited[ny][nx]:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                              

max_cnt = 1 
for k in range(h+1):
    
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                bfs(i, j, k)
                cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)