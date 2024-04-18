# 백준 2615_오목
# 완전탐색

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]
# visited = [False * 19 for _ in range(19)]

# 4가지 방향 체크
# 하, 우, 대각선왼아래, 대각선오위
dy=[1,0,1,-1]
dx=[0,1,1,1]

def solution():
    for y in range(19):
        for x in range(19):
            if board[y][x] != 0:
                color = board[y][x] # 색 저장

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    cnt = 1
                    while 0 <= ny < 19 and 0 <= nx < 19 and board[ny][nx] == color:
                        cnt += 1
                        # print(cnt)
                        if cnt == 5:
                            # 육목인지 확인
                            if 0 <= x - dx[i] < 19 and 0 <= y-dy[i] < 19 and board[y-dy[i]][x-dx[i]] == color:
                                break
                            if 0 <= nx + dx[i] < 19 and 0 <= ny+dy[i] < 19 and board[ny+dy[i]][nx+dx[i]] == board[ny][nx]:
                                break
                            return color, y, x
                        
                        ny += dy[i]
                        nx += dx[i]
    return 0,-1,-1

result, y, x = solution()
print(result)
if result > 0:
    print(y+1, x+1)