# 백준 5800_성적 통계
# implementation

import sys
input = sys.stdin.readline

k = int(input())

for i in range(1, k+1):
    score = list(map(int, input().split()))
    cnt = score[0]
    score = score[1:]
    score.sort()
    
    lg = 0 # Largest gap 0으로 초기화
    for j in range(0, cnt - 1):
        if score[j+1] - score[j] > lg: # 인접한 점수의 차이가 lg보다 크면
            lg = score[j+1] - score[j] # 해당 값을 저장
    print(f'Class {i}')
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {lg}')