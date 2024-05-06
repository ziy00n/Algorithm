# 백준 4963_섬의 개수
# BFS

import sys
from collections import deque
input = sys.stdin.readline


dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, 1, 1, -1, -1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = True

    while q:
        y, x = q.popleft()       
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # 범위 확인, 1인지(땅인지) 확인, visited 여부 확인
            if 0 <= ny < h and 0 <= nx < w:
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    q.append([ny, nx])
                    visited[ny][nx] = True


while True:
    w, h = map(int, input().split())
    visited = [[False] * w for _ in range(h)]
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    cnt = 0
    
    if w == 0 and h == 0: break
    
    else:
        for i in range(h):
            for j in range(w):
                if visited[i][j] == False and graph[i][j] == 1:
                    bfs(i,j)
                    cnt += 1
        
        print(cnt)