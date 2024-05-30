# 백준 2210_숫자판 점프
# DFS

import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
answer = set()

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(y, x, lst):
    if len(lst) == 6:
        str_lst = ''.join(map(str, lst))
        if str_lst not in answer:
            answer.add(str_lst)
        return
    
    else:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny< 5 and 0<=nx<5:
                dfs(ny, nx, lst+[graph[ny][nx]])
                
    
for i in range(5):
    for j in range(5):
        dfs(i,j,[graph[i][j]])

# print(answer)
print(len(answer))