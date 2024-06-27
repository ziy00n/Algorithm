# 백준 9375_패션왕 신해빈
# 자료구조

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cloth = dict()
    answer = 1
    n = int(input())
    for _ in range(n):
        name, type = input().rstrip().split()

        if type in cloth:
            cloth[type] += 1
        else:
            cloth[type] = 1

    for i in cloth:
        answer *= (cloth[i] + 1)

    print(answer - 1)