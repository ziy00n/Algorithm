# 백준 1743_음식물 피하기
# BFS

import sys
input = sys.stdin.readline

from collections import deque

n, m, k = map(int, input().split())

graph = [[0] * (m+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1


dy = [-1,1,0,0]
dx = [0,0,-1,1]

visited = [[False] * (m+1) for _ in range(n+1)]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 < ny <= n and 0 < nx <= m:
                if visited[ny][nx] == False and graph[ny][nx] == 1:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                    cnt += 1
    
    return cnt

max_cnt = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if not visited[i][j] and graph[i][j] == 1:
            cnt = bfs(i, j)
            max_cnt = max(cnt, max_cnt)

print(max_cnt)