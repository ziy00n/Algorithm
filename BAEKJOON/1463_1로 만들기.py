import sys
input = sys.stdin.readline

N = int(input())

# dp리스트 : 인덱스 i 에 대해서 i를 1로 만들기 위한 연산의 최소 횟수
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])




