# 백준 1012_유기농 배추
# BFS

import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스
T = int(input())

def bfs(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]    
    
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == False and graph[ny][nx] == 1:
                    q.append([ny, nx])
                    visited[ny][nx] = True
      
      
result = []
for _ in range(T):
    m, n, k = map(int, input().split())
    
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    # print(graph)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(i,j)
                cnt += 1
    result.append(cnt)
                

for i in result:
    print(i)