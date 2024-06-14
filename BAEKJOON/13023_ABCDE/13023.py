# 백준 13023_ABCDE
# DFS, 백트래킹

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

friend = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

visited = [False] * n

flag = False
def dfs(k, cnt):
    global flag
    
    if cnt == 5:
        flag = True
        return
    
    for i in friend[k]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False
    if flag:
        break

if flag:
    print(1)
else:
    print(0)