# 백준 10026_적록색약
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [list(input().rstrip()) for _ in range(n)]
# print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
def bfs(y,x): # 그래프 돌면서 graph[y][x]의 색과 같은 색인 노드를 visited True로 변경(한 뭉터기 색)
    queue.append([y,x])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        # print(y, x)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == False and graph[ny][nx] == graph[y][x]:
                    queue.append([ny,nx])
                    visited[ny][nx] = True

# 적록색약 X
cnt = 0
visited = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if visited[y][x] == False:
            bfs(y,x)
            cnt += 1

# 적록색약으로 전환
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
# print(graph)

#적록색약
cnt2 = 0
visited = [[False] * n for _ in range(n)] # visited 초기화
for y in range(n):
    for x in range(n):
        if visited[y][x] == False:
            bfs(y,x)
            cnt2 += 1 

print(cnt, cnt2, sep=' ')