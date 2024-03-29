# 백준 1520_내리막 길
# DFS + DP

import sys
# sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

m, n = map(int, input().split()) 

graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)] # 세로 m, 가로 n

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#DFS
def dfs(y, x):
    if y == (m-1) and x == (n-1):
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] < graph[y][x]:
            cnt += dfs(ny,nx)

    dp[y][x] = cnt
    return dp[y][x]

print(dfs(0,0))