# 백준 13305_주유소
# 그리디

import sys
input = sys.stdin.readline

n = int(input())

dis = list(map(int, input().split()))
price = list(map(int, input().split()))

minPrice = price[0]
ans = 0
for i in range(n-1):
    if minPrice > price[i]:
        minPrice = price[i]
    ans += minPrice * dis[i]

print(ans)