# 백준 13549_숨바꼭질 3
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001

q = deque()
q.append(n)
visited[n] = 0

def bfs(a):
    while q:
        a = q.popleft()
        if a == k:
            print(visited[a])
            break
        
        else:
            for i in [2*a, a-1, a+1]:
                if 0 <= i <= 100000 and visited[i] == 0:
                    q.append(i)
                    if i == (2*a):
                        visited[i] = visited[a]
                    else:
                        visited[i] = visited[a] + 1                    
    
bfs(n)