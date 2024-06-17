# 백준 2343_기타 레슨

import sys
input = sys.stdin.readline
 

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
L  = max(arr)
R = sum(arr)

while L <= R:
    mid = (L+R)//2

    count = 0 
    sum = 0
    for i in range(N):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]
    if sum:
        count += 1

    if count > M:
        L = mid + 1
    else:
        R = mid - 1
        answer = mid

print(answer)