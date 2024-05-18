# 백준 18352_특정 거리의 도시 찾기
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 도시 x에서 출발하여 최단 거리 k인 도시들을 구한 후 도시 번호 오름차순 출력
result = []
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1
                
                if distance[i] == k:
                    result.append(i)

bfs(x)

# 결과
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)