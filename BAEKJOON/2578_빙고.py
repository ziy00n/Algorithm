# 백준 2578_빙고
# implementation

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]

order = []
for _ in range(5):
    order += list(map(int, input().split())) # 사회자가 부르는 수-> 1차원 리스트로 저장

def bingo():
    bingo_cnt = 0

    # 가로
    for v in visited:
        if v.count(1) == 5:
            bingo_cnt += 1
    
    # 세로
    for x in range(5):
        y_cnt = 0
        for y in range(5):
            if visited[y][x] == 1:
                y_cnt +=1 
        
        if y_cnt == 5:
            bingo_cnt += 1
    
    # 왼쪽 위 대각선
    d1 = 0
    for k in range(5):
        if visited[k][k] == 1:
            d1 += 1
    if d1 == 5:
        bingo_cnt += 1

    # 오른쪽 위 대각선
    d2 = 0
    for k in range(5):
        if visited[k][4-k] == 1:
            d2 += 1
    if d2 == 5:
        bingo_cnt += 1
    
    return bingo_cnt

cnt = 0
for i in range(25):
    for y in range(5):
        for x in range(5):
            if order[i] == board[y][x]:
                visited[y][x] = 1
                cnt += 1

    if cnt >= 12:
        result = bingo()
        if result >= 3:
            print(i+1)
            break 