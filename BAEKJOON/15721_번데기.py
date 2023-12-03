# 백준 15721_번데기
# 완전 탐색

import sys
input = sys.stdin.readline

A = int(input()) 
T = int(input())
say = int(input())

bcount = 0
dcount = 0 

cnt = 0 

N = []          

while True:

    cnt += 1

    for _ in range(2):
        bcount += 1
        N.append((bcount, 0))
        dcount += 1
        N.append((dcount, 1))
    for _ in range(cnt + 1):
        bcount += 1
        N.append((bcount, 0))
    for _ in range(cnt + 1):
        dcount += 1
        N.append((dcount, 1))

    if bcount >= T:
        print(N.index((T, say)) % A)
        break