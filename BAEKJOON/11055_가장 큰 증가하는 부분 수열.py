# 백준 11055_가장 큰 증가하는 부분 수열 - https://www.acmicpc.net/problem/11055
# DP

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [x for x in A]

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])
        # if A[i] > A[j] and dp[i] < dp[j] + A[i]:
        #     dp[i] = dp[j]+A[i]

print(max(dp))