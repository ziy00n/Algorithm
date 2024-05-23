# 백준 15656_N과 M (7)
# 백트래킹

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def dfs(lst):
    if len(lst) == M:
        print(*lst)
        return
    
    for i in range(len(arr)):
        dfs(lst+[arr[i]])

dfs([])