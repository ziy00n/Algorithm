# 백준 1238_파티
# 다익스트라

import sys, heapq
input = sys.stdin.readline

# 정점n, 간선m, 모이는 마을x
n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(s, x):
    q = []
    heapq.heappush(q, [0, s])
    # 각자 집에서 하나씩 구해야하므로 함수가 초기화될 때마다 최단거리테이블도 초기화
    distance = [1e9] * (n+1)
    distance[s] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 인접노드 node[0]: 정점번호, node[1]:시간
        for node in graph[now]:
            cost = node[1] + dist
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    
    return distance[x]


arr = []
for i in range(1, n+1):
    # 각자 집(i)에서 x마을까지 최단경로 + x마을에서 각자 집(i)로 돌아오는 최단경로
    arr.append(dijkstra(i, x) + dijkstra(x, i))
    
arr.sort()
print(arr[-1]) # 시간 최대값