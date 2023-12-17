# 백준 17626_Four Squares
# DP

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)  # 자연수 1부터 시작, 인덱스 맞춰주기
dp[1] = 1

for i in range(2, N + 1):
    minimum = sys.maxsize

    # 1부터 탐색
    for j in range(1, int(i ** 0.5) + 1):
        minimum = min(minimum, dp[i - (j ** 2)])
    dp[i] = minimum + 1

print(dp[N])