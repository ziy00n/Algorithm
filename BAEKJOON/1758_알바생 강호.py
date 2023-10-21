# 백준 1758_알바생 강호
# 그리디

import sys
input = sys.stdin.readline

n = int(input())
arr = []
tips = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True) # 팁이 큰 순서대로 내림차순 정렬


for i in range(n):
    if arr[i] - (i-1) > 0:
        tips += arr[i] - i
    else:
        break
print(tips)