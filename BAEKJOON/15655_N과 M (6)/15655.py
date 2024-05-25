# 백준 15655_N과 M (6)
# 백트래킹

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def dfs(k, lst):
    if len(lst) == M:
        print(*lst)
        return
    
    for i in range(k, len(arr)):
        dfs(i+1, lst+[arr[i]])

dfs(0, [])