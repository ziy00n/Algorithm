# 백준 15654_N과 M (5)

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N개 자연수, 길이 M

arr = list(map(int, input().split()))
arr.sort() # 사전순
visited = [0] * (N)

def dfs(lst):
    if len(lst) == M:
        print(*lst)
        return
    
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            dfs(lst+[arr[i]])
            visited[i] = 0

dfs([])