# 백준 11722_가장 긴 감소하는 부분 수열 - https://www.acmicpc.net/problem/11722
# DP

import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))

dp = [1] * n # 나 혼자만 부분 수열이어도 길이는 1이므로

for i in range(n):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1) # 앞 숫자(j)의 부분 수열의 길이+1 = i의 부분 수열 길이

print(max(dp))