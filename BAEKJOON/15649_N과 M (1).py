# 백준 15649_N과 M (1)
# 백트래킹
# 백트래킹으로 순열 구현

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []

for i in range(1, n+1):
    nums.append(i)

arr = [] # 순열 담는 배열

def dfs():
    if len(arr) == m:
        print(*arr)
    else:
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
                dfs()
                arr.pop()
                
dfs()