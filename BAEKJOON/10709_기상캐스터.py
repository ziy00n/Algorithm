# 백준 10709_기상캐스터
# implementation

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
board = [list(input().rstrip()) for _ in range(h)]

cloud_time = 1 # 처음 구름이 오는 시간
is_cloud = False # 바로 전에 구름이 떠있었는지

for i in range(h):
    for j in range(w):

        if board[i][j] == 'c': # 구름
            board[i][j] = 0
            is_cloud = True
            cloud_time = 1

        elif board[i][j] == '.' and is_cloud == False: # 바로 전에 구름 X
            board[i][j] = -1

        elif board[i][j] == '.' and is_cloud == True: # 바로 전에 구름 O
            board[i][j] = cloud_time
            cloud_time += 1

    cloud_time = 1
    is_cloud = False

    print(*board[i])