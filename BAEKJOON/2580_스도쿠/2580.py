# 백준 2580_스도쿠
# 백트래킹

import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append([i,j])
            

def row(y,x,n):
    for i in range(9):
        if n == arr[y][i]:
            return False
    return True
    
def col(y,x,n):
    for i in range(9):
        if n == arr[i][x]:
            return False
    return True
    
def square(y,x,n):
    ny = (y//3) * 3
    nx = (x//3) * 3
    
    for i in range(3):
        for j in range(3):
            if n == arr[ny+i][nx+j]:
                return False
    return True
            
flag = False
def dfs(bidx):
    global flag
    if flag == True:
        return
    if bidx == len(blank):
        for i in arr:
            print(*i)
        flag = True
        return
    
    y, x = blank[bidx][0], blank[bidx][1]
    for i in range(1,10):
        if row(y,x,i) and col(y,x,i) and square(y,x,i):
            arr[y][x] = i
            dfs(bidx+1)
            arr[y][x] = 0

dfs(0)