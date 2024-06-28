# 백준 1717_집합의 표현
# 자료구조

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int,input().split())
parents = [i for i in range(n+1)]

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')