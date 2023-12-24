# 백준 2231_분해합
# Brute Force

import sys
input = sys.stdin.readline

N = int(input())
x = 0
for i in range(N):
    a = list(map(int, str(i)))
    if N == sum(a) + i:
        x = i
        break;
print(x)