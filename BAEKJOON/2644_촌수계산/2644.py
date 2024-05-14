# 백준 2644_촌수계산
# BFS

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split()) # a, b 의 촌수 계산
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

# 인접리스트
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    

def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[v] + 1
                
bfs(a)

if visited[b] != 0:
    print(visited[b]-1)
else:
    print(-1)