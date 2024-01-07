# 백준 2776_암기왕
# Data Stucture

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    list1 = set(map(int, input().split()))
    m = int(input())
    list2 = list(map(int, input().split()))
    for num in list2:
        print(1 if num in list1 else 0)