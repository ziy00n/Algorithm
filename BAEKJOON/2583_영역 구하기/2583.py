# 백준 2583_영역 구하기
# BFS

# 그림을 오른쪽으로 90도 돌리면 board 좌표 잡기가 편함

import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

board = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    # 그림 오른쪽 90도 회전했다고 생각
    # x1,x2 -> y축 역할, y1,y2 -> x축 역할
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):     # 왼쪽 위 꼭짓점부터
        for j in range(y1, y2): # 오른쪽 아래 꼭짓점까지
            board[i][j] = 1

dy = [-1,1,0,0]
dx = [0,0,-1,1]

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
            
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == False and board[ny][nx] == 0:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                    cnt += 1
    return cnt
    
    
area_list = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and visited[i][j] == False:
            area = bfs(i,j)
            area_list.append(area)

area_list.sort()

print(len(area_list))
print(*area_list)