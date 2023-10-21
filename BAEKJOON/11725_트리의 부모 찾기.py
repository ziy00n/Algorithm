# 백준 11725_트리의 부모 찾기
# 트리 / 그래프 탐색

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N + 1)] 
parent = [0] * (N + 1) 

for _ in range(N - 1):  # 간선의 갯수 = 노드 개수 - 1
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)


dfs(1)

for j in range(2, N+1):
    print(parent[j])