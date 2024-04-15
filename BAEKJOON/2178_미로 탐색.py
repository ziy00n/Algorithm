# 백준 2178_미로 탐색
# BFS

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

q = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(r, c):
    global cnt
    cnt = 0 
    
    # 탐색 시작 노드
    q.append([r,c])
    visited[r][c] = True

    while q:
        queueSize = len(q)
        cnt += 1
        for _ in range(queueSize):
            y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny <= (n-1) and 0 <= nx <= (m-1)  and not visited[ny][nx] and maze[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append([ny, nx])
            
            if y == (n-1) and x == (m-1):
                q.clear()
                break
    
    return cnt

print(bfs(0,0))