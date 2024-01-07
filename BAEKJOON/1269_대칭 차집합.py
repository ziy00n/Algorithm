# 백준 1269_대칭 차집합
# 자료구조

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

print(len(a_set - b_set) + len(b_set - a_set))