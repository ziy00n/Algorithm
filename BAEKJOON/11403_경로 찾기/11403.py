# 백준 11403_경로 찾기
# BFS

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def bfs(s):
    q = deque()
    q.append(s)
    check = [0] * N
    
    while q:
        x = q.popleft()
        
        for i in range(N):
            if check[i] == 0 and graph[x][i] == 1:
                q.append(i)
                visited[s][i] = 1
                check[i] = 1
                
for i in range(N):
    bfs(i)

for row in visited:
    print(*row)