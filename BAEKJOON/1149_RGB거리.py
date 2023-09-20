#1149_RGB거리

import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0] # R : 이전 것이 G,B 중 더 작은 것 
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1] # G : 이전 것이 R,B 중 더 작은 것
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2] # B : 이전 것이 R,G 중 더 작은 것

print(min(arr[-1][0], arr[-1][1], arr[-1][2]))