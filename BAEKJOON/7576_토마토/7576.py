# 백준 7576_토마토
# BFS

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

# BFS 풀 때 visited 사용여부 생각하고 풀기
# visited 사용 X
# visited = [[0] * M for _ in range(N)]

q = deque()
def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny<N and 0<=nx<M:
                if box[ny][nx] == 0:
                    q.append([ny, nx])
                    box[ny][nx] = box[y][x] + 1
                
                
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append([i, j])


bfs()

max_day = 0
for i in box:
    if 0 in i:
        max_day = -1
        break
    max_day = max(max(i), max_day)
    
if max_day == 1:
    print(0)
elif max_day == -1:
    print(-1)
else:
    print(max_day-1)