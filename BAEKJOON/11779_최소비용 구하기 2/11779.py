# 백준 11779_최소비용 구하기 2
# 다익스트라

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) 


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (N+1)
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                parents[next_node] = now
                heapq.heappush(q, (cost, next_node))
    
    return distance

start, end = map(int, input().split())
parents = [0] * (N+1)

dist_start = dijkstra(start)

print(dist_start[end])

path = []
curr = end
while curr:
    path.append(curr)
    curr = parents[curr]

path.reverse()
print(len(path))
print(*path)