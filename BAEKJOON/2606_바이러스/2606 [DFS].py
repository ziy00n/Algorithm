# 백준 2606_바이러스
# DFS

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

tree = dict()
seen = set()

# 딕셔너리 초기화
for i in range(1, n+1):
    tree[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cnt = 0
def dfs(k):
    global cnt
    seen.add(k)
    
    items = tree[k]
    
    for item in items:
        if item not in seen:
            dfs(item)
            cnt += 1
    
dfs(1)
print(cnt)