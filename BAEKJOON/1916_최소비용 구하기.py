# 백준 1916_최소비용 구하기
# 다익스트라

import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

# 시작노드, 도착노드, 가중치
for i in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

# 구하고자하는 구간의 출발점, 도착점
start, end = map(int, input().split())

# 현재 최단 경로
dist = [1e9] * (N+1) # 최댓값이 10억 미만이라면 무한(INF)의 값으로 1e9 사용

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        current_cost, node = heapq.heappop(q)
    
        # 저장되어있던 최단 거리(dist[node])보다 큐에 있던 현재 가중치(current_cost)가 크면 방문했던 노드
        # => 무시
        if current_cost > dist[node]:
            continue # 무시
        
        for next_cost, next_node in graph[node]:
            total_next_cost = current_cost + next_cost
            
            if total_next_cost < dist[next_node]: # 더 작게 걸리면 
                
                dist[next_node] = total_next_cost # 기존보다 더 최단 경로이므로 교체
                
                # 다음에 갈 후보 heapq에 추가
                heapq.heappush(q, (total_next_cost, next_node))
    # return dist[end]

dijkstra(start)
print(dist[end])