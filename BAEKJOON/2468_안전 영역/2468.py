# 백준 2468_안전 영역
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

m_height = 0
for row in board:
    m_height = max(max(row), m_height)


dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == False and board[ny][nx] != 0:
                q.append([ny, nx])
                visited[ny][nx] = True


result = []
for k in range(0, m_height):
    
    for a in range(n):
        for b in range(n):
            if board[a][b] <= k:
                board[a][b] = 0
    
    visited = [[False] * n for _ in range(n)]
    
    safe_cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and visited[i][j] == False:
                bfs(i,j)
                safe_cnt += 1
    result.append(safe_cnt)

print(max(result))