# 백준 7568_덩치
# implementation 
# Brute Force

import sys
input = sys.stdin.readline

N = int(input())
people = []

for _ in range(N):
    x, y = map(int, input().split()) # x: 몸무게, y: 키
    people.append([x,y]) # 2차원 배열 [[x1, y1], [x2, y2] ...]

for p in people: # p: 현재 비교 대상, op : p와 비교할 나머지 사람들
    rank = 1
    for op in people:
        if p[0] < op[0] and p[1] < op[1]: # 현재 비교하는 p보다, 다른 사람 op 의 몸무게 & 키가 더 크면
            rank += 1 # 등수 + 1
    print(rank, end=' ') # p의 등수

"""
# 몸무게, 키 각각 리스트 만들어 담기
# 위 방법보다 시간 단축
          
import sys
input = sys.stdin.readline

N = int(input())
w, h = [0] * N, [0] * N

for i in range(N):
  w[i], h[i] = map(int, input().split())

for i in range(N):
  ranking = 1
  for j in range(N):
    if w[i] < w[j] and h[i] < h[j]:
      ranking += 1
  print(ranking, end=" ")
"""