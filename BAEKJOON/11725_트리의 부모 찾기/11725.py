# 백준 11725_트리의 부모 찾기
# DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) # 재귀 깊이 제한

n = int(input())

tree = dict()
seen = set()

for i in range(1, n+1):
    tree[i] = []

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


parent = [0] * (n+1) # 부모 저장

def dfs(k):
    seen.add(k)
    
    items = tree[k]
    
    for item in items:
        if item not in seen:
            parent[item] = k
            dfs(item)


dfs(1)

for i in range(2, n+1):
    print(parent[i])