# 백준 1303_전쟁 - 전투
# BFS

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, c):
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < m and 0 <= nx < n:
                if visited[ny][nx] == False and graph[ny][nx] == c:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                    cnt += 1   
    return cnt * cnt

result = [0, 0] # [0] W위력의 합, [1] B위력의 합
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                result[0] += bfs(i, j, 'W')
            else:
                result[1] += bfs(i, j, 'B')
                
print(*result)



'''
## ======================
## [정답코드] 
## 처음에 시도한 방법 : 딕셔너리에 저장, graph의 값이 'B'인 것에 대해 첫번째 BFS, 'W'인 것에 대해 두번째 BFS ##

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(m)]
# print(graph)
visited = [[False] * n for _ in range(m)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(y, x, c):
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < m and 0 <= nx < n:
                if visited[ny][nx] == False and graph[ny][nx] == c:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                    cnt += 1   
    return cnt

result = {'B': 0, "W": 0}

for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 'W':
            cnt = bfs(i, j, 'W')
            cnt *= cnt
            result['W'] += cnt

for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 'B':
            cnt = bfs(i, j, 'B')
            cnt *= cnt
            result['B'] += cnt

print(result['W'], result['B'])

'''