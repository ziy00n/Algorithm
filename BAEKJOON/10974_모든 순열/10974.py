# 백준 10974_모든 순열
# 백트래킹

n = int(input())

arr = [i for i in range(1, n+1)]
visited = [0 for _ in range(n)]

def dfs(lst):
    if len(lst) == n:
        print(*lst)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(lst+[arr[i]])
            visited[i] = 0
        
dfs([])