# 프로그래머스 네트워크
# 코딩테스트 고득점 Kit 깊이/너비 우선 탐색(DFS/BFS)
# Lv.3
# BFS

from collections import deque

def solution(n, computers):
    visited = [False] * n
    q = deque()
    cnt = 0
    # 첫 그룹(노드별로 전부 확인)
    for i in range(n):
        if visited[i] == False: # 이미 방문했다면 다음 노드(i+1)로
            q.append(i) # 0번 노드부터 시작
            cnt += 1
        while q: # 큐 빌 때까지
            r = q.popleft() # 노드 r 탐색
            for j in range(n):
                # 탐색하는 노드랑 연결된 노드 찾기(아직 방문 X & r과 연결된)
                if visited[j] == False and computers[r][j] == 1:
                    q.append(j)
                    visited[j] = True
    return cnt