# 백준 1697_숨바꼭질
# BFS

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001

def bfs(v):
    queue = deque([v])
    
    while queue:
        v = queue.popleft()
        if v == k:
            print(visited[v])
            break

        for next in [v-1, v+1, 2*v]:
            if 0 <= next <= 100000 and visited[next] == 0:
                queue.append(next)
                visited[next] = visited[v] + 1

bfs(n)


'''
# 처음 풀이
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
#graph = [[] for _ in range(100001)]
#visited = [False] * 100001
visited = [0] * 100001
#command = [(n+1), (n-1), (2*n)]

#second = 0
def bfs(n):
    #global second
    #second = 0
    queue = deque([n])
    #visited[n] = True
    
    while queue:
        v = queue.popleft()
        #second += 1
        #visited[n] = True
        #second += 1
        #print("second ++ ")
        if v == k:
            #print('v == k')
            #print(second)
            print(visited[v])
            break

        for i in [v+1, v-1, 2*v]:
            if 0 <= i <= 100000 and visited[i] == 0:
                #second += 1
                #print("second ++ ")
                queue.append(i)
                #visited[i] = True
                visited[i] = visited[v] + 1
        #     graph[v].append(i)
        # for j in graph[v]:
            # if not visited[j]:
            #     queue.append(j)
            #     visited[j] = True

bfs(n)

'''