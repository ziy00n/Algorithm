# 백준 10974_모든 순열
# 백트래킹

# 1. 백트래킹 dfs 이용
n = int(input())
nums = [i for i in range(1, n+1)]
visited = [False for _ in range(n)]
arr = []

def dfs(depth):
    if depth == n:
        print(*arr)
    else:
        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                arr.append(nums[i])
                dfs(depth+1)
                visited[i] = False
                arr.pop()

dfs(0)


'''
# 2. itertools 이용 # 

from itertools import permutations

n = int(input())
nums = [i for i in range(1, n+1)]
arr = list(permutations(nums, n))

for i in arr:
    print(*i)

'''