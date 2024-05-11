# 백준 1926_그림
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

picture = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,1,-1]

def bfs(y, x):
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and picture[ny][nx] == 1:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                    cnt += 1
    return cnt 
    
    
result = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and picture[i][j] == 1:
            area = bfs(i,j)
            result.append(area)

picture_cnt = len(result)
print(picture_cnt)

if picture_cnt == 0:
    print(0)
else:
    print(max(result))