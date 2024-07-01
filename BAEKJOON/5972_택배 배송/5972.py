# 백준 5972_택배 배송
# 다익스트라

import sys, heapq
INF = int(1e9)

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dijkstra(s):
    q = []
    distance = [1e9] * (n+1)
    distance[s] = 0
    heapq.heappush(q, [0, s])

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = next_cost + dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, [cost, next_node])

    return distance

distance = dijkstra(1)
print(distance[n])