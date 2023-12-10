# 백준 2847_게임을 만든 동준이
# 그리디
import sys
input = sys.stdin.readline

N = int(input())
score = []
cnt = 0

for _ in range(N):
    score.append(int(input()))

for i in range(N - 1, 0, -1):
    if score[i] <= score[i - 1]:
        cnt += (score[i - 1] - score[i] + 1)
        score[i - 1] = score[i] - 1

print(cnt)