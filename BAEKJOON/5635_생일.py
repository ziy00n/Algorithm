# 백준 5635_생일
# implementation

import sys
input = sys.stdin.readline

n = int(input()) # 학생 수
arr = []

for _ in range(n):
    student = input().split()
    arr.append(student)
    # arr.append(input().split())

arr.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1]))) #년(x[3])기준 정렬, 같을 경우 월(x[2]) -> 일(x[1]) 순서로 오름차순 정렬

print(arr[-1][0]) # 가장 나이 많은 학생(arr 마지막 인덱스)
print(arr[0][0]) # 가장 나이 적은 학생