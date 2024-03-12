# 백준 집합 11723_집합
# implementation

import sys
input = sys.stdin.readline

M = int(input())
S = set() # 집합

for _ in range(M):
    cal = input().split()
    if cal[0] == 'add':
        if int(cal[1]) not in S:
            S.add(int(cal[1]))
    elif cal[0] == 'remove': 
        if int(cal[1]) in S:
            S.remove(int(cal[1]))
        # S.discard(int(cal[1]))
    elif cal[0] == 'check':
        if int(cal[1]) in S:
            print(1)
        else:
            print(0)
    elif cal[0] == 'toggle':
        if int(cal[1]) in S:
            S.remove(int(cal[1]))
        else:
            S.add(int(cal[1]))
    elif cal[0] == 'all':
        S = {i for i in range(1, 21)}
    elif cal[0] == 'empty':
        S = set()