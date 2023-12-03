# 백준 14247_나무 자르기
# 그리디
import sys
input = sys.stdin.readline

N = int(input())                        #나무의 개수(벌목할 일자)
h = list(map(int, input().split()))     #나무의 길이들
speed = list(map(int,input().split()))  #나무의 성장속도

arr = []
total = 0

for i in range(N):                  # 나무의 초깃값(길이)과 성장속도를 2차원 배열에 담아준다.
    arr.append([speed[i], h[i]])

arr.sort()

for i in range(N):
    total += arr[i][0] * i + arr[i][1]

print(total)