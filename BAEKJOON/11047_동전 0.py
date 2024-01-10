import sys
input = sys.stdin.readline

n,k = map(int, input().split())

coins = []
for j in range(n):
    coins.append(int(input()))
    
coins.sort(reverse=True)
result = 0

for i in coins:
    result += k // i
    k %= i

print(result)