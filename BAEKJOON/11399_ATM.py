# 백준 11399_ATM
# 그리디

import sys
input = sys.stdin.readline

n = int(input())

minutes = sorted(list(map(int, input().split())))
result = 0

for x in range(1, n+1):
    result += sum(minutes[0:x])

print(result)