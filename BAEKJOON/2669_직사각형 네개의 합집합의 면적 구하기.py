# 백준 2669_직사각형 네개의 합집합의 면적 구하기
# implementation

import sys
input = sys.stdin.readline

board = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1
# print(board)
            
result = 0
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            result += 1
print(result)