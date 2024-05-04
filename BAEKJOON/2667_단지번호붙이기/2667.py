# 백준 2667_단지번호붙이기
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x] = True
   
    cnt = 1
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == False:
                if graph[ny][nx] == 1:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                    cnt += 1
    return cnt 

result = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == False and graph[i][j] == 1:
            home_cnt = bfs(i,j)
            result.append(home_cnt)

result.sort()

danji_cnt = len(result)
print(danji_cnt)

for hc in result:
    print(hc)