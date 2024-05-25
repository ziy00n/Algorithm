# 프로그래머스 코딩테스트 고득점 Kit_게임 맵 최단거리
# 깊이/너비 우선 탐색(DFS/BFS)
# Lv.2
# BFS

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    q = deque()
    q.append([0,0])
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # n x m 범위 넘어가면 무시
            # 항상 범위 검사가 첫번째
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            
            # 벽이면 무시
            if maps[ny][nx] == 0:
                continue
            
            # 방문 안한 곳이면
            if maps[ny][nx] == 1:
                q.append([ny, nx])
                maps[ny][nx] = maps[y][x] + 1
            
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    


'''
# 2. visit 를 통해 방문여부 체크하는 방법으로 구현 # 

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # print(n, m)
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    
    while q:
        queueSize = len(q)
        cnt += 1
        for _ in range(queueSize):
            y, x = q.popleft()

            if y == (n-1) and x == (m-1):
                return cnt
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                # n x m 범위 넘어가면 무시
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue

                # 벽이면 무시
                if maps[ny][nx] == 0:
                    continue

                # 방문 안한 곳이면
                if visited[ny][nx] == False and maps[ny][nx] == 1:
                    q.append([ny, nx])
                    visited[ny][nx] = True

    return -1
    
'''