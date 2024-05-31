# 백준 2178_미로 탐색
# BFS

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs():
    q = deque()
    q.append([0,0])
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if maze[ny][nx] == 1:
                    q.append([ny, nx])
                    maze[ny][nx] = maze[y][x] + 1

bfs()

# print(maze)
print(maze[n-1][m-1])