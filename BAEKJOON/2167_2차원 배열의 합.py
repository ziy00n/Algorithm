# 백준 2167_2차원 배열의 합
# implementation

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())

for _ in range(k):
    x, y , a, b = list(map(int, input().split()))
    sum_arr = 0
    for i in range(x-1, a):
        for j in range(y-1, b):
            sum_arr += arr[i][j]
    print(sum_arr)