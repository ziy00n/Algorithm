# 백준 18110_solved.ac
# implementation

import sys
input = sys.stdin.readline

n = int(input())

def Round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

if n == 0:
    print(0)
else:
    score = []
    for i in range(n):
        score.append(int(input().rstrip()))
    score.sort()

    start = Round(n * 0.15)  # 제외되어야 하는 사람의 수
    score = score[start:n - start]   # 제외될 사람 빼고, 평균 계산할 범위
    
    print(Round(sum(score) / len(score)))