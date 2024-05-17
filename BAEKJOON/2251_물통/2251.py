# 백준 2251_물통
# BFS, 완전탐색


from collections import deque

A, B, C = map(int, input().split())

visited = [[False] * (B+1) for _ in range(A+1)]

q = deque()
q.append([0,0]) # 처음 시작 시 C만 가득 차있는 상태로 시작 a:0, b:0, c:z 의 양
visited[0][0] = True

# pour함수 : x -> y 으로 물을 옮긴 후 상태를 큐에 저장 & 방문처리
# pour() 의 인자는 물이 옮겨진 뒤의 A 물의 양 x, B 물의 양y (C의 양 z은 x, y로 알 수 있음)
def pour(x, y):
    if not visited[x][y]:
        q.append([x, y]) # A, B 물통의 현재 물의 양 큐에 넣기
        visited[x][y] = True # 방문처리

result = []  
def bfs():
    while q:
        x, y = q.popleft()
        z = C - x - y # 용량C인 물통의 현재 물의 양 z
        
        if x == 0: # A물통의 물 양 0이면 z 저장
            result.append(z)
        
        # 물 옮기는 방법 6가지
        # x->y
        water = min(x, B-y) # x->y로 옮길 물의 양 (x전체 OR B 물통 꽉 채우기(B-y))
        pour(x-water, y+water)
        # x->z
        water = min(x, C-z)
        pour(x-water, y)
        # y->x
        water = min(y, A-x)
        pour(x+water, y-water)
        # y->z
        water = min(y, C-z)
        pour(x, y-water)
        # z->x
        water = min(z, A-x)
        pour(x+water, y)
        # z->y
        water = min(z, B-y)
        pour(x, y+water)
        

bfs()

result.sort()
print(*result)