# 백준 2740_행렬 곱셈
# implementation, 수학

# 행렬 곱
# A행렬 n x m B행렬 m x k 일 때, A * B = n x k

import sys
input = sys.stdin.readline

A=[]
B=[]
n, m = map(int, input().split())
for _ in range(n):
    A.append(list(map(int, input().split())))

m, k = map(int, input().split())
for _ in range(m):
    B.append(list(map(int, input().split())))

AB = [[0] * k for _ in range(n)] # 최종 행렬 : A의 행 X B의 열 0으로 초기화
for i in range(n):
    for j in range(k):
        for a in range(m):
            AB[i][j] += A[i][a] * B[a][j]

for i in AB:
    print(*i)