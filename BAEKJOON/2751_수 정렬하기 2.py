# 백준 2751_수 정렬하기 2
# 정렬

import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
# print(arr)
arr.sort()
for i in arr:
    print(i)