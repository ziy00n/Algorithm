# 백준 1926_그림
# BFS

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

visited = [[False] * m for _ in range(n)]

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
            
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and picture[ny][nx] == 1:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                    cnt += 1
    
    return cnt      
                    
                    
result = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and picture[i][j] == 1:
            cnt = bfs(i,j)
            result.append(cnt)


picture_cnt = len(result)
print(picture_cnt)
if picture_cnt == 0:
    print(0)
else:
    print(max(result))