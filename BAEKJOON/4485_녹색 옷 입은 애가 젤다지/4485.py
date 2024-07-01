# 백준 4485_녹색 옷 입은 애가 젤다지?
# 다익스트라

import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        dist, x, y = heapq.heappop(q)

        if x == N - 1 and y == N - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))


count = 1

while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    dijkstra()
    count += 1