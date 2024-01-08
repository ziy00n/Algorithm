# 백준 9625_BABBA
# DP

import sys
input = sys.stdin.readline

k = int(input())

dp = [[0,0] for _ in range(k+1)] # A, B 개수

dp[0][0]=1
#dp[0][1]=0

for i in range(1, k+1):
    dp[i][0] = dp[i-1][1] # A의 개수 = 이전 클릭의 B의 개수
    dp[i][1] = dp[i-1][0] + dp[i-1][1] # B의 개수 = 이전 클릭의 A의 개수

print(dp[i][0], dp[i][1]) 