# 백준 8979_올림픽
# implementation

import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 국가의 수 n, 등수 알고 싶은 국가 k

arr = []
for _ in range(n):
    j, g, s, b = map(int, input().split())
    arr.append([j, g, s, b])

rank_list = []
for i in arr:
    ranking = 1
    for j in arr:
        if i[1] < j[1]:
            ranking += 1
        elif i[1] == j[1] and i[2] < j[2]:
            ranking += 1
        elif i[1] == j[1] and i[2] == j[2] and i[3] < j[3]:
            ranking += 1
    rank_list.append([i[0], ranking])


for i in range(len(rank_list)):
    if rank_list[i][0] == k:
        print(rank_list[i][1])