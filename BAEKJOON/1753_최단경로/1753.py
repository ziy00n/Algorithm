# 백준 1753_최단경로
# 다익스트라

import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]

distance = [1e9] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    # 단방향, a에서 b로 가는 가중치 c
    graph[a].append([b,c])

def dijkstra(k):
    q = []
    heapq.heappush(q, (0, k))
    distance[k] = 0
    while q:
        # 최단 거리 가장 짧은 노드의 거리, 노드번호 꺼내기
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        # i[0]:노드번호, i[1]: 거리
        for i in graph[now]:
            c = dist + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(q, (c, i[0])) # 갱신된 (거리,노드) 우선순위큐에 추가

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])