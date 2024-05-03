# 백준 2606_바이러스
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# BFS로 탐색
visited = [False] * (n+1)

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True

    cnt = 0
    while q:
        x = q.popleft() # 1이 뽑힘
        # cnt += 1
        if len(graph[x]) != 0:
            for i in graph[x]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
                    
    return cnt # 1번 노드가 웜 바이러스 전염시킨 컴퓨터 수
    
print(bfs(1))