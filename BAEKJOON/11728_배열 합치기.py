# 백준 11728_배열 합치기
# Sorting

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = A + B
# print(result)
result.sort()

print(*result)