# 백준 17086_아기 상어 2
# BFS

## - 상어의 위치부터 각 좌표의 거리를 구하는 방법- ##
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [-1,1,0,0,-1,-1,1,1]
dx = [0,0,-1,1,1,-1,-1,1]

# 큐에 아기 상어의 좌표 삽입
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])


# 상어에서부터 각 좌표를 탐색해서 거릿값 계산
def bfs():
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                    graph[ny][nx] = graph[y][x] + 1
    
    
bfs()

max_dist = 0
for row in graph:
    max_dist = max(max_dist, max(row))

print(max_dist-1)

# map 함수 이용해서 2차원 리스트 내의 최대원소 출력
# print(max(map(max, graph))-1)