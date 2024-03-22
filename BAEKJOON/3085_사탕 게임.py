# 백준 3085 사탕 게임
# implementation

import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

max_cnt = 0
# 최대 사탕 개수 찾기
def find():
    # 행 별로 최대값 찾기
    global max_cnt
    for y in range(n):
        row_cnt = 1 # 초기 개수 1로 초기화
        for x in range(1, n):
            if board[y][x] == board[y][x-1]: # 같은 행의 사탕이 그 전 꺼랑 같으면
                row_cnt += 1
                max_cnt = max(max_cnt, row_cnt) # 현재 row_cnt 와 기존 최대 사탕개수를 비교하여 큰 값을 대입
        
            else: # 다르면
                row_cnt = 1 # 그 행의 cnt = 1 로 초기화
    
    # 열 마다 최대값 찾기
    for x in range(n):
        col_cnt = 1
        for y in range(n-1):
        # for y in range(1, n):
            if board[y+1][x] == board[y][x]:
                col_cnt += 1
                max_cnt = max(max_cnt, col_cnt)
            else:
                col_cnt = 1    


for y in range(n):
    for x in range(n):
        # 1. 오른쪽칸과 바꾸기
        if x+1 < n:
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
            find() # 최대값 찾기
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x] # 원상복구
        # 2. 아래칸과 바꾸기 
        if y+1 < n:
            board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
            find()
            board[y][x], board[y+1][x] = board[y+1][x], board[y][x]

print(max_cnt)