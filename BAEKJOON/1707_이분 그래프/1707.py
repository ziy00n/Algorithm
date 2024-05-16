# 백준 1707_이분 그래프
# BFS

import sys
from collections import deque
input = sys.stdin.readline

k = int(input()) # 테스트케이스 개수

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 1
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == False: # 아직 방문 X
                q.append(i)
                visited[i] = -1 * visited[node] # 상위 정점과 다른 집합으로 저장
            elif visited[i] == visited[node]: # 만약 방문했었는데 상위 정점과 같은 집합이면(1 or -1)
                return False
    return True # 위의 조건에 안걸리면 True        
    
    
# 테스트케이스 k개
for _ in range(k):
    v, e = map(int, input().split()) # v:정점 개수, e:간선개수
    
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1) # False:미방문, 서로다른 두집합 : 1, -1  
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, v+1):
        if visited[i] == False:
            result = bfs(1) # 해당 i 노드에 대해 BFS
            if result == False:
                break
            
    if result == False:
        print('NO')
    else:
        print('YES')