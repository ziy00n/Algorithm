# 백준 2491_수열
# implementation

import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [1] * n # 증가하는 수열
dp2 = [1] * n # 감소하는 수열

for i in range(1, n):
    if nums[i] > nums[i-1]:
        dp[i] = dp[i-1] + 1
        dp2[i] = 1
    elif nums[i] < nums[i-1]:
        dp2[i] = dp2[i-1] + 1
        dp[i] = 1
    elif nums[i] == nums[i-1]:
        dp2[i] = dp2[i-1] + 1
        dp[i] = dp[i-1] + 1

dp_m = max(dp) 
dp2_m = max(dp2)

if dp_m >= dp2_m:
    print(dp_m)
else:
    print(dp2_m)