# 백준 1913_달팽이
# implementation

import sys
input = sys.stdin.readline

n = int(input())
X = int(input())

board = [[0] * n for _ in range(n)]

x = y = n//2
board[y][x] = 1 # 가운데 시작 1 저장

dy=[-1,0,1,0] # board의 좌표상 상->우->하->좌 순
dx=[0,1,0,-1]

repeat = 1 # repeat: 상우하좌가 2번씩 1번반복,2번반복, 3번반복 이렇게 늘어남
# 상, 우, / 하, 하, 좌, 좌,/ 상,상,상, 우,우,우, /하,하,하,하,  좌좌좌좌, / 상상상상상, ...
i = 0
num = 2 # 1은 이미 넣었고, 2부터 n제곱까지 +1 하면서 저장할 것
answer = [y+1, x+1]
while x!= 0 or y!=0:
    flag = 0
    for _ in range(2): # 2번
        for _ in range(repeat): 
            y = y + dy[i]
            x = x + dx[i]
            board[y][x] = num
            if num == X:
                # answer.append([y+1, x+1])
                answer = [y+1, x+1]
            if x == 0 and y == 0:
                flag = 1 
                break
            num += 1 # num=2,3,4, ... n^2
        if flag == 1:
            break
        i = (i+1)%4
    repeat += 1

for i in board:
    print(*i)
print(*answer)