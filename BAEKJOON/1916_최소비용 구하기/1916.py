# 백준 1916_최소비용 구하기
# 다익스트라

import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b, c]) # a->b 로 가는 가중치 c

# 출발도시 s, 도착도시 e 
s, e = map(int, input().split())

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q) # 최소힙 pop-> dist가 가장 작은 노드 

        if distance[now] >= dist:
            for i in graph[now]:
                if i[1] + dist < distance[i[0]]:
                    distance[i[0]] = i[1] + dist # 최단테이블 갱신
                    heapq.heappush(q, (distance[i[0]], i[0])) # 갱신된 (거리, 노드번호) 우선순위큐 삽입

                            
dijkstra(s)
print(distance[e])