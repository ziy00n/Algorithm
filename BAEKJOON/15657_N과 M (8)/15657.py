# 백준 15657_N과 M (8)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

def dfs(k, lst):
    if len(lst) == m:
        print(*lst)
        return
    
    for i in range(k, len(arr)):
        dfs(i, lst+[arr[i]])
    
dfs(0, [])