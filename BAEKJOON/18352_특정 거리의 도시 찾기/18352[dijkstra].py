# 백준 18352_특정 거리의 도시 찾기
# 다익스트라

import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(s):
    q = []
    heapq.heappush(q, [0, s])
    distance[s] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(x)

answer = []
for j in range(1, n+1):
    if distance[j] == k:
        answer.append(j)

if len(answer)==0:
    print(-1)
else:
    for i in answer:
        print(i, end='\n')