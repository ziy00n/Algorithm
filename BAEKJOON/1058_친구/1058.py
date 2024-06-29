# 백준 1058_친구
# BFS

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

def bfs(v):
    visited = [False] * n
    q = deque([[v, 0]])
    visited[v] = True
    cnt = 0
    while q:
        a, b = q.popleft()
        
        if b >= 2:
            continue
        
        for i in range(n):
            if not visited[i] and graph[a][i] == 'Y':
                q.append([i, b+1])
                visited[i] = True
                cnt += 1
                
    return cnt


answer = 0
for i in range(n):
    answer = max(answer, bfs(i))

print(answer)