#2748_피보나치 수 2

N = int(input())

dp = [0]*(N+1)

dp[1]=1 # 0,1 로 시작되도록 초기화

for i in range(2, N+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N])