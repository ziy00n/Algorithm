# 백준 1652_누울 자리를 찾아라
# implementation

import sys
input = sys.stdin.readline

n = int(input())

room = [list(input().rstrip()) for _ in range(n)]

#가로 줄
row_cnt = 0
for y in range(n):
    cnt = 0
    for x in range(n):
        if room[y][x] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            row_cnt += 1

# 세로 줄
col_cnt = 0
for x in range(n):
    cnt = 0
    for y in range(n):
        if room[y][x] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            col_cnt += 1

print(row_cnt, col_cnt)