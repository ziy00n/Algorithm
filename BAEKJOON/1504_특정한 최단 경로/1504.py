# 백준 1504_특정한 최단 경로
# 다익스트라

import sys, heapq
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

# 1번에서 v1,v2를 거쳐서 n번 정점까지 가는 최단 경로
# 방법1) 1->v1->v2->n
# 방법2) 1->v2->v1->n
def dijkstra(s, e):
    q = []
    heapq.heappush(q, (0, s))
    distance = [INF] * (n+1)
    distance[s] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance[e]


path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

answer = min(path1, path2)

if answer >= INF:
    print(-1)
else:
    print(answer)