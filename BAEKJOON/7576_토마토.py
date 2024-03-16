# 백준 7576_토마토
# BFS

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


queue = deque()
visited = [[False] * m for _ in range(n)]

for row in range(n):
    for col in range(m):
        if graph[row][col] == 1:
            queue.append([row, col])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        v = queue.popleft()
        visited[v[0]][v[1]] = True

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[v[0]][v[1]] + 1  #graph 중 가장 큰 값이 마지막으로 익은 토마토까지 걸린 일 수-1
                    queue.append([nx, ny])
                    visited[nx][ny] = True

bfs()

cnt = 0
for row in graph:
    for i in row:
        if i == 0:  # 익지 않은 토마토(0)가 존재하면 -1 출력
            print(-1)
            exit(0) # 종료
    cnt = max(cnt, max(row))# 한 줄씩 최댓값을 찾아서 최댓값 갱신

print(cnt-1) # graph 시작이 1부터 였는데 시작일은 0 이므로 -1 한 값이 걸린 날짜